import tkinter as tk
from tkinter import filedialog
import csv
import requests
import json
import user_attribute
import tensorflow_hub as hub
from scipy.spatial import distance

# Insightly API Key
pod = 'na1'
insightlyAPIkey = "2749c36f-192d-423b-ab08-e9b793299427"
insightlyAPIurl = "https://api.{}.insightly.com/v3.1".format(pod)
eirIndustryField = "CONTACT_FIELD_127"
eirSkillsField = "CONTACT_FIELD_128"

def getProjectNames(filepath):
    #Gets the project's name from the CSV generated from Qualtrics
    try:
        names = []
        with open(filepath) as project:
            reader = csv.DictReader(project)
            for row in reader:
                if row["Startup Name"]:
                    names.append(row["Startup Name"])
    except csv.Error as e:
        return e
    return names

def getProjectIndustry(filepath):
    #Gets the project's closest industry from the CSV generated from Qualtrics
    try:
        industries = []
        with open(filepath) as project:
            reader = csv.DictReader(project)
            for row in reader:
                if row['Industry']:
                    industries.append(row['Industry'])
    except csv.Error as e:
        return e
    return industries

def getProjectDesc(filepath):
    #Gets the project's description from the CSV generated from Qualtrics
    try:
        with open(filepath) as projectFile:
            reader = csv.reader(projectFile)
            header = []
            header = next(reader)
            header = next(reader)
            desc = []
            #had to do it like this because the column we need for the description is #Q67, however there is another column Q67 that will overwrite the info that we need
            for row in reader:
                if row[30]:
                    desc.append(row[30])
    except csv.Error as e:
        return e
    return desc

def getIndustrySet():
    #import industry text file and parse it for the industries
    industrySet = set()
    with open("Industries.txt") as industryFile:
        industryData = industryFile.readline()
        industryData.lstrip("{").rstrip("}")
        industryData = industryData.split(", ")
        for i, industries in enumerate(industryData):
            industryData[i] = industries.strip("'")
        industrySet = set(industryData)
        return industrySet

def getSkillSet():
    #import skills text file and parse it for the skills
    skillSet = set()
    with open("skillSets.txt") as skillsFile:
        skillsData = skillsFile.readline()
        skillsData.lstrip("{").rstrip("}")
        skillsData = skillsData.split(", ")
        for i, skills in enumerate(skillsData):
            skillsData[i] = skills.strip("'")
        skillSet = set(skillsData)
    return skillSet

def getMergeList():
    industry_list = list(getIndustrySet())
    skill_list = list(getSkillSet())
    merge_list = industry_list + skill_list
    return merge_list, len(industry_list) + 2

def getEmbed(loader, embed_list):
    embeddings = loader(embed_list)
    return embeddings

def getSimilarity(name, embedding, new_merge_list, industry_len):
    # find best match industry
    final_ind = ""
    final_ind_score = -100
    final_skill = ""
    final_skill_score = -100
    embed_index = -1
    if name == new_merge_list[0]:
        embed_index = 0
    elif name == new_merge_list[1]:
        embed_index = 1
    for i in range(2, industry_len):
        matching_ind = 1 - distance.cosine(embedding[embed_index], embedding[i])
        if matching_ind > final_ind_score:
            final_ind = new_merge_list[i]
            final_ind_score = matching_ind
    for j in range(industry_len, len(new_merge_list)):
        matching_skill = 1 - distance.cosine(embedding[embed_index], embedding[j])
        if matching_skill > final_skill_score:
            final_skill = new_merge_list[j]
            final_skill_score = matching_skill
    return [final_ind, final_ind_score, final_skill, final_skill_score]

def getMentor(p, loader, ind_skill_list, industry_len):
    project = p
    new_merge_list = ind_skill_list[:]
    industry = project.get_industry()
    description = project.get_description()
    new_merge_list.insert(0, description)
    new_merge_list.insert(0, industry)
    # embed the list into tensorflow
    embedding = getEmbed(loader, new_merge_list)

    # get the best match of industry and skill
    matching_list = getSimilarity(industry, embedding, new_merge_list, industry_len)
    final_ind = matching_list[0]
    final_ind_score = matching_list[1]
    final_skill = matching_list[2]
    final_skill_score = matching_list[3]

    # get mentors
    industry_set = set(getIndustryContacts(final_ind))
    skill_set = set(getSkillsContacts(final_skill))
    merged_contact_list = list(industry_set.intersection(skill_set))
    if 0 < len(merged_contact_list) <= 5:
        project.add_mentors(merged_contact_list)
    elif 0 < len(industry_set) <= 5:
        project.add_mentors(list(industry_set))
    elif 0 < len(skill_set) <= 5:
        project.add_mentors(list(skill_set))
    else:
        matching_list = getSimilarity(description, embedding, new_merge_list, industry_len)
        final_ind = matching_list[0]
        final_ind_score = matching_list[1]
        final_skill = matching_list[2]
        final_skill_score = matching_list[3]
        industry_set = set(getIndustryContacts(final_ind))
        skill_set = set(getSkillsContacts(final_skill))
        merged_contact_list = list(industry_set.intersection(skill_set))
        if 0 < len(merged_contact_list) <= 5:
            project.add_mentors(merged_contact_list)
        elif 0 < len(industry_set) <= 5:
            project.add_mentors(list(industry_set))
        elif 0 < len(skill_set) <= 5:
            project.add_mentors(list(skill_set))
        elif len(merged_contact_list) > 5:
            project.add_mentors(merged_contact_list[:5])
        elif len(industry_set) > 5:
            project.add_mentors(list(industry_set)[:5])
        elif len(skill_set) > 5:
            project.add_mentors(list(skill_set)[:5])
        else:
            return project
    return project

def getIndustryContacts(fieldvalue):
    #Calls on the insightly API to get contacts who have the fieldvalue within their EiR Industries
    r = requests.get(insightlyAPIurl + "/Contacts/Search?" + "field_name=" + eirIndustryField + "&field_value=" + fieldvalue + "&brief=false&count_total=false", auth = (insightlyAPIkey, ''))
    insightlyJson = r.json()
    names = []
    for contacts in insightlyJson:
        if contacts["FIRST_NAME"] and contacts["LAST_NAME"]:
            names.append(contacts["FIRST_NAME"] + f" {contacts['LAST_NAME']}")
    return names

def getSkillsContacts(fieldvalue):
    #Calls on the insightly API to get contacts who have the fieldvalue within their EiR Skills
    r = requests.get(insightlyAPIurl + "/Contacts/Search?" + "field_name=" + eirSkillsField + "&field_value=" + fieldvalue + "&brief=false&count_total=false", auth = (insightlyAPIkey, ''))
    insightlyJson = r.json()
    names = []
    for contacts in insightlyJson:
        if contacts["FIRST_NAME"] and contacts["LAST_NAME"]:
            names.append(contacts["FIRST_NAME"] + f" {contacts['LAST_NAME']}")
    return names

def run():
    # index of industry: [2: industry_set_len], index of skill: [industry_set_len:]
    merge_list, industry_list_len = getMergeList()

    # load tensorflow
    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

    # get names, industry and descriptions
    project_name_list = getProjectNames(projectFilePath)[1:]
    project_industry_list = getProjectIndustry(projectFilePath)[1:]
    project_description_list = getProjectDesc(projectFilePath)

    user_class_list = []
    for i in range(len(project_name_list)):
        name = project_name_list[i]
        industry = project_industry_list[i]
        description = project_description_list[i]
        user_class = user_attribute.Project(name, industry, description)
        new_user_class = getMentor(user_class, embed, merge_list, industry_list_len)
        user_class_list.append(new_user_class)
    return user_class_list


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    projectFilePath = filedialog.askopenfilename(filetypes=[("CSV","*.csv")])
    project_class_list = run()
    for p in project_class_list:
        print("Project name:", p.get_name())
        print("Matching mentors:", str(p.get_mentor())[1:-1])
