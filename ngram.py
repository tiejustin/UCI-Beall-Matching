import tensorflow_hub as hub
from scipy.spatial import distance
import time


def get_industries(file):
    with open(file, "r") as f:
        ind_set = eval(f.readline().strip())
        return ind_set


def get_skill_set(file):
    with open(file, "r") as f:
        skill_set_set = eval(f.readline().strip())
        return skill_set_set


def get_similarity(sentence, ind_list):
    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
    ind_list.insert(0, sentence)
    embeddings = embed(ind_list)
    final_ind = ""
    final_score = -100
    for i in range(1, len(ind_list)):
        matching_score = 1 - distance.cosine(embeddings[0], embeddings[i])
        if matching_score > final_score:
            final_ind = ind_list[i]
            final_score = matching_score
    similarity_dic = {final_ind: final_score}
    return similarity_dic


''' industry_sorted_dic = {}
    for ind, rank in sorted(similarity_dic.items(), key=lambda x: x[1], reverse=True):
        industry_sorted_dic[ind] = rank
    print(industry_sorted_dic)'''


def get_designated_score(industry_dic, designated_index):
    industry_name = list(industry_dic.keys())[designated_index]
    print(industry_name, industry_dic[industry_name])
    return industry_name


def get_match_mentor(industry_name, mentor_dic):    # mentor_dic = {mentor_name: [industry1, industry2]}
    whole_mentor_list = []
    for mentor_name in mentor_dic:
        if industry_name in mentor_dic[mentor_name]:
            whole_mentor_list.append(mentor_name)
    return whole_mentor_list


def process(name, skills, mentors, index):   # index: get the # highest score of industry
    similar_dic = get_similarity(name, skills)
    if index >= len(similar_dic) and similar_dic != {}:
        return -1   # return -1 if the index is greater than the length of similar_dic
    industry = get_designated_score(similar_dic, index)
    match_mentor_list = get_match_mentor(industry, mentors)
    return match_mentor_list


if __name__ == "__main__":
    start = time.time()
    print("Program Start")
    skill_set = get_skill_set("../../Insightly/skillSets.txt")
    print(skill_set)
    '''
    user_keyword = "Business Productivity"
    user_description = "Shaka is an online platform that helps companies keep their employees engaged whether they are working in the office or at home."
    industry_list = get_industries("Industries.txt")
    skill_list = get_skill_set("skillSets.txt")
    industry_list += skill_list
    mentors_dic = {"a": ["Business Development"],
                   "b": ["Business Development"],
                   "c": ["E-Commerce/ Retail", "Health and Fitness"]}

    number = 0
    mentor_list = process(user_keyword, skill_list, mentors_dic, number)
    print(mentor_list)
    if len(mentor_list) > 5:
        mentor_list = process(user_description, skill_list, mentors_dic, number)
    end = time.time()
    print("Total execution time: " + str(end - start) + " seconds.")'''

