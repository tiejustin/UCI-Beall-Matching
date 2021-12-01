import requests
import json
import csv
import tkinter as tk
import Decoder
import logHandler
import APIKeyFunction
from datetime import datetime
from tkinter import filedialog
import sys

logObject = logHandler.LogHandler()

def getNum(file_path):
    # print("getNum is being called")
    file_name = file_path
    # print("file_path pass in:" , file_path)
    # print("file_name got:" , file_name)
    row = 0
    count = 0
    with open(file_name, 'r') as f:
        csv_reader = csv.reader(f)
        for rows in csv_reader:
            if (row >= 2):
                count += 1
            row += 1
    return count
    
def getUCIAffiliation(uci_affiliation, json_dict2):
    returnJsonDict = []
    if ('9' in uci_affiliation):  # if no affiliation, set all text to "na"
        json_dict2['CUSTOMFIELDS'] = {}
        json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_154'
        json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = "na"
        json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_154'
        returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
        json_dict2['CUSTOMFIELDS'] = {}
        json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_133'
        json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = "na"
        json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_133'
        returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
        json_dict2['CUSTOMFIELDS'] = {}
        json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_82'
        json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = "na"
        json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_82'
        returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
        json_dict2['CUSTOMFIELDS'] = {}
        json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_142'
        json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = "na"
        json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_142'
        returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
        json_dict2['CUSTOMFIELDS'] = {}
        json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_18'
        json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = "na"
        json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_18'
        returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
        json_dict2['CUSTOMFIELDS'] = {}
        json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'UCI_unit__c'
        json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = None
        json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'UCI_unit__c'
        returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
    else:
        if ('1' in uci_affiliation):  # UCI student
            json_dict2['CUSTOMFIELDS'] = {}
            json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_154'
            json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = "UCI student"
            json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_154'
            returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
        if ('2' in uci_affiliation):  # UCI student alum
            json_dict2['CUSTOMFIELDS'] = {}
            json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_133'
            json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = "UCI student alum"
            json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_133'
            returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
        if ('3' in uci_affiliation):  # UCI faculty
            json_dict2['CUSTOMFIELDS'] = {}
            json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_82'
            json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = "Current"
            json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_82'
            returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
        if ('4' in uci_affiliation):  # UCI staff
            json_dict2['CUSTOMFIELDS'] = {}
            json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_23'
            json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = True
            json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_23'
            returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
        if ('5' in uci_affiliation):  # Relatives of UCI community
            json_dict2['CUSTOMFIELDS'] = {}
            json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_132'
            json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = True
            json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_132'
            returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
            # NOTES: Add Local Business Executive and Local Service Provider here by modifying the field name and field ID
            # Local Business Executive
            # if ('6' in uci_affiliation):
            #     json_dict2['CUSTOMFIELDS'] = {}
            #     json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_xxx'
            #     json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = True
            #     json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_xxx'
            #     json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS'])
            # Local Service Provider
            # if ('7' in uci_affiliation):
            #     json_dict2['CUSTOMFIELDS'] = {}
            #     json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_xxx'
            #     json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = True
            #     json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_xxx'
            #     json_dict['CUSTOMFIELDS'].append(json_dict2['CUSTOMFIELDS']

    return returnJsonDict

def academicDecoder(academic_area, json_dict2):
    academic_decoder = {
        1: ";Claire Trevor School of the Arts"
        , 2: ";Francisco J. Ayala School of Biological Sciences"
        , 3: ";The Paul Merage School of Business"
        , 5: ";The Henry Samueli School of Engineering"
        , 6: ";School of Humanities"
        , 7: ";Donald Bren School of Information and Computer Sciences"
        , 9: ";School of Law"
        , 10: ";School of Medicine"
        , 13: ";School of Physical Sciences"
        , 16: ";School of Social Sciences"
        , 18: ";Teaching & Learning"
        , 19: ";Office of Research"
        , 4: ";School of Education"
        , 8: ";Interdisciplinary Studies"
        , 11: ";Sue & Bill Gross School of Nursing"
        , 12: ";Department of Pharmaceutical Sciences"
        , 14: ";Program in Public Health"
        , 15: ";School of Social Ecology"
        , 17: ";Extension"
        , 20: ";CALIT2"
        , 21: ";UC Irvine Health"
        , 22: ";Beckman Laser Institute"
    }
    str1 = ""
    for i in academic_area:
        str1 += academic_decoder[int(i)]
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'UCI_unit__c'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = str1
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'UCI_unit__c'
    return json_dict2['CUSTOMFIELDS']

def getOrganization(insightlyAPIurl, insightlyAPIkey, organizationResponses, rownum):
    organization_id = None
    r = requests.get(
        insightlyAPIurl + '/Organisations/Search?field_name=ORGANISATION_NAME&field_value=' + organizationResponses + '&brief=false&count_total=false', auth=(insightlyAPIkey, ''))
    organization_json = r.json()
    if (organization_json): # if list is  not empty, it means ORGANISATION_ID exists
        organization_json = organization_json[0]  # first item in list is the organization dict
        organization_id = int(organization_json['ORGANISATION_ID'])
        # json_dict2['CUSTOMFIELDS'] = {}
        # json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'ORGANISATION_ID'
        # json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = int(organization_json['ORGANISATION_ID'])
        # json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'ORGANISATION_ID'
    else:
        logObject.writeNotification(rownum, "organization not found")
    # Print log statement that Organization does not exist in Insightly
    
    # else:
    #     print('Organization name not found for ORGANISATION_NAME: ' + row['Organization 1_1']) 
    return organization_id

def getIndustryEiR(industryResponses, json_dict2):
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_127'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = Decoder.decodeIndustry(industryResponses)
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_127'
    return json_dict2['CUSTOMFIELDS']

def getSkillEiR(skillResponses, json_dict2):
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_128'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = Decoder.decodeSkills(skillResponses)
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_128'
    return json_dict2['CUSTOMFIELDS']

def getGender(genderResponses, json_dict2):
    gender_decoder = {
        1: "Male"
        , 2: "Female"
        , 3: "Non-Binary / Third Gender"
        , 4: "Prefer Not to Say"
    }
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'Gender__c'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = gender_decoder[int(genderResponses)]
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'Gender__c'
    return json_dict2['CUSTOMFIELDS']

def getEthnicity(ethnicityResponses, json_dict2):
    ethnicity = []
    ethnicity.extend(ethnicityResponses.split(","))
    ethnicity = list(set(ethnicity))  # remove duplicated
    ethnicity_decoder = {
        1: ";American Indian / Alaskan Native"
        , 2: ";Asian / Asian American"
        , 3: ";Black, non-Hispanic"
        , 4: ";Hispanic / LatinX"
        , 5: ";Native Hawaiian / Pacific Islander"
        , 6: ";White, non-Hispanic"
        , 7: ";Southwest Asian, Middle Eastern or North African"
        , 8: ";Prefer not to Say"
    }
    str1 = ""
    for i in ethnicity:
        str1 += ethnicity_decoder[int(i)]
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'Ethnicity__c'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = str1
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'Ethnicity__c'
    return json_dict2['CUSTOMFIELDS']

def getAcademicOther(academicOtherText, json_dict2):
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_151'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = academicOtherText
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_151'
    return json_dict2['CUSTOMFIELDS']

def getMotivations(motivationValues, json_dict2):
    returnJsonDict = []
    # Motivation_1
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_92'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = motivationValues[0]
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_92'
    returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
    
    # Motivation_2
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_93'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = motivationValues[1]
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_93'
    returnJsonDict.append(json_dict2['CUSTOMFIELDS'])

    # Motivation_2
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_94'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = motivationValues[2]
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_94'
    returnJsonDict.append(json_dict2['CUSTOMFIELDS'])

    # Motivation_4
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_95'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = motivationValues[3]
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_95'
    returnJsonDict.append(json_dict2['CUSTOMFIELDS'])

    # Motivation_5
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_96'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = motivationValues[4]
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_96'
    returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
    
    return returnJsonDict

def getAcademicBackground(academicInfo, json_dict2):
    background = academicInfo[0] + ' - ' + academicInfo[1] + ' - ' + academicInfo[2]
    if (academicInfo[3]):
        background += '; ' + academicInfo[3] + ' - ' + academicInfo[4] + ' - ' + academicInfo[5]
        if (academicInfo[6]):
            background += '; ' + academicInfo[6] + ' - ' + academicInfo[7] + ' - ' + academicInfo[8]
            if (academicInfo[9]):
                background += '; ' + academicInfo[9] + ' - ' + academicInfo[10] + ' - ' + academicInfo[11]
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_129'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = background
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_129'
    
    return json_dict2['CUSTOMFIELDS']

def getAdditionalContactInfo(contactInfo, json_dict2):
    returnJsonDict = []
    # Contact_9
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_143'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = contactInfo[0]
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_143'
    returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
    # Contact_10
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_144'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = contactInfo[1]
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_144'
    returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
    # Contact_11
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_145'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = contactInfo[2]
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_145'
    returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
    
    return returnJsonDict

def getUCIStaff(uci_staff_str, json_dict2):
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_142'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = uci_staff_str
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_142'
    return json_dict2['CUSTOMFIELDS']

def getWorkshop(workshop, json_dict2):
    returnJsonDict = []
    eir_workshop = []
    eir_workshop.extend(workshop[0].split(","))
    eir_workshop = list(set(eir_workshop))  # remove duplicated
    eir_workshop_decoder = {
        1: ";Legal basics"
        , 2: ";Finance and accounting fundamentals"
        , 3: ";Team formation"
        , 4: ";Market validation"
        , 5: ";Sales and marketing"
        , 6: ";Presentation and pitching skills"
        , 7: ";Soft skills and networking"
        , 8: ";Design thinking"
        , 9: ";Funding sources"
        , 10: ";Tech basics / entrepreneur tools"
        , 11: "Others"  # manually added this, not in selection for Insightly
    }
    str1 = ""

    for i in eir_workshop:
        if (i != '11'):
            str1 += eir_workshop_decoder[int(i)]
        else:  # "Other, please specify:"
            if (workshop[1]):
                json_dict2['CUSTOMFIELDS'] = {}
                json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_126'
                json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = workshop[1]
                json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_126'
                returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'EiR_Potential_Workshop_Presenter__c'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = str1
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'EiR_Potential_Workshop_Presenter__c'
    returnJsonDict.append(json_dict2['CUSTOMFIELDS'])
    return returnJsonDict

def getLL(llResponses, json_dict2):
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'CONTACT_FIELD_146'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = llResponses
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'CONTACT_FIELD_146'
    return json_dict2['CUSTOMFIELDS']

def getAIOpp(Opp, json_dict2):
    returnJsonDict = []
    eir_role = []
    eir_role.extend(Opp[0].split(","))
    eir_role = list(set(eir_role))
    eir_role_decoder = {
        2: ";Wayfinder advisor"
        , 1: ";Wayfinder contributor"
        , 3: ";Grant proposal reviewer"
        , 5: ";Campus resource"
        , 6: ";Competition judge"
        , 7: ";Campus team mentor"
        , 8: ";General coach"
        , 4: ";Lunch and Learn speaker"
    }
    str1 = ""
    for i in eir_role:
        str1 += eir_role_decoder[int(i)]
    if (Opp[1]):  # Wayfinder Opp exists if "1" is chosen from AI Opp
        eir_role2 = Opp[1].split(",")
        eir_role2 = list(set(eir_role2))  # remove duplicated
        eir_role_decoder2 = {
            3: ";Wayfinder app consultant;Wayfinder admission interviewer"
            , 4: ";Wayfinder orientation leader"
            , 2: ";Wayfinder advisor"
            , 5: ";Wayfinder instructor"
            , 6: ";Wayfinder reviewer"
        }
        for i in eir_role2:
            if (i == "2" and "2" in eir_role):  # avoid duplication because same value
                continue
            str1 += eir_role_decoder2[int(i)]
    json_dict2['CUSTOMFIELDS'] = {}
    json_dict2['CUSTOMFIELDS']['FIELD_NAME'] = 'EiR_Desired_Role_From_Survey__c'
    json_dict2['CUSTOMFIELDS']['FIELD_VALUE'] = str1
    json_dict2['CUSTOMFIELDS']['CUSTOM_FIELD_ID'] = 'EiR_Desired_Role_From_Survey__c'
    return json_dict2['CUSTOMFIELDS']

def main(file_path, rownum, start, end):
    # error message pass back to window
    message = ""
    # Insightly API Key
    pod = 'na1'
    insightlyAPIkey = APIKeyFunction.APIKey()
    insightlyAPIurl = "https://api.{}.insightly.com/v3.1".format(pod)

    try:
        # CSV Source
        file_name = file_path
        imported_count = 0
        # Get last saved datetime
        with open("savedData.txt", "r") as file:
            saveddate = file.readline()
            lastdate = datetime.strptime(saveddate, '%Y-%m-%d %H:%M:%S')
            # if not saveddate:
            #     useLastDate = 0
            # else:
            #     lastdate = datetime.strptime(saveddate, '%Y-%m-%d %H:%M:%S')
            #     useLastDate = 1
            # file.close()
            
        # Get data from CSV and transfer
        with open(file_name, newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            for i, rows in enumerate(reader):
                if i == rownum:
                    row = rows
                    # print(rownum, row)

            if int(row["Progress"]) != 100:
                #print("progress return")
                logObject.writeIncompleteResponse(rownum, row["Progress"])
                return message, imported_count
            # convert start and end time
            start_date = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
            end_date = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
          

            # Check if datetime is valid to extract data from

            try:
                date_time_obj = datetime.strptime(row["RecordedDate"], '%Y-%m-%d %H:%M:%S')
            except ValueError:
                try:
                    date_time_obj = datetime.strptime(row["RecordedDate"], '%m/%d/%Y %H:%M')
                except Exception as e:
                    logObject.writeError(rownum, e, "was encountered when converting date formats")
                    return message, imported_count # Message?
            

            # if useLastDate:
            # if lastdate >= date_time_obj:
            #     print("lastdate return")
            #     return message, imported_count
            
            # check time frame
            if start_date >= date_time_obj or end_date < date_time_obj:
                logObject.writeNotInDateRange(rownum)
                # print("start_date:", start_date)
                # print("date:", date_time_obj)
                # print("end_date:", end_date)
                return message, imported_count
            
            json_dict = {"CONTACT_ID": None, "FIRST_NAME": row['Contact_1']}
            json_dict['CUSTOMFIELDS'] = []
            json_dict2 = {}

            # Section 1: Involvement Opportunities
            if (row['AI Opp']):
                Opp = [row['AI Opp'], row['Wayfinder Opps']]
                json_dict['CUSTOMFIELDS'].append(getAIOpp(Opp, json_dict2))

            if (row['Wayfinder Workshop']):
                workshop = [row['Wayfinder Workshop'], row['Wayfinder Workshop_11_TEXT']]
                json_dict['CUSTOMFIELDS'].extend(getWorkshop(workshop, json_dict2))

            if (row['L&L']):
                json_dict['CUSTOMFIELDS'].append(getLL(row['L&L'], json_dict2))

            # Section 2: Motication for Participating
            if (row['Motivations_1']):
                motivations = [int(row['Motivations_1']), int(row['Motivations_2']), int(row['Motivations_3']), int(row['Motivations_4']) ,int(row['Motivations_5'])]
                json_dict['CUSTOMFIELDS'].extend(getMotivations(motivations, json_dict2))

            # Section 3: Industry
            if (row['Industry']):
                json_dict['CUSTOMFIELDS'].append(getIndustryEiR(list(row.values())[27:56], json_dict2))

            # Section 4: Skill Set / Areas of Expertise
            if (row['Skills']):
                json_dict['CUSTOMFIELDS'].append(getSkillEiR(list(row.values())[56:67], json_dict2))

            # Section 5: Career Background
            if (row['Organization 1_1']):
                json_dict['ORGANISATION_ID'] = getOrganization(insightlyAPIurl, insightlyAPIkey.getAPI(), row['Organization 1_1'], rownum)
                
            if (row['Organization 1_2']):
                json_dict['TITLE'] = row['Organization 1_2']

            # Section 6: Academic Background (Brian)
            if (row['Degree 1_1']):
                academicInfo = [row['Degree 1_1'], row['Degree 1_2'], row['Degree 1_3'],
                                row['Degree 2_1'], row['Degree 2_2'], row['Degree 2_3'],
                                row['Degree 3_1'], row['Degree 3_2'], row['Degree 3_3'],
                                row['Degree 4_1'], row['Degree 4_2'], row['Degree 4_3']]
                json_dict['CUSTOMFIELDS'].append(getAcademicBackground(academicInfo, json_dict2))
            
            if (row['Academic - Other']):
                json_dict['CUSTOMFIELDS'].append(getAcademicOther(row['Academic - Other'], json_dict2))
                
            # Section 7: Contact Information
            if (row['Contact_2']):
                json_dict['LAST_NAME'] = row['Contact_2']
            if (row['Contact_4']):
                json_dict['PHONE'] = row['Contact_4']
            if (row['Contact_3']):
                json_dict['EMAIL_ADDRESS'] = row['Contact_3']
            if (row['Contact_5']):
                json_dict['ADDRESS_MAIL_STREET'] = row['Contact_5']
            if (row['Contact_6']):
                json_dict['ADDRESS_MAIL_CITY'] = row['Contact_6']
            if (row['Contact_7']):
                json_dict['ADDRESS_MAIL_STATE'] = row['Contact_7']
            if (row['Contact_8']):
                json_dict['ADDRESS_MAIL_POSTCODE'] = row['Contact_8']
            
            if (row['Contact_9']):
                extraInfo = [row['Contact_9'], row['Contact_10'], row['Contact_11']]
                json_dict['CUSTOMFIELDS'].extend(getAdditionalContactInfo(extraInfo, json_dict2))
                
            # Section 7: Demographics
            if (row['Q100']):
                json_dict['CUSTOMFIELDS'].append(getGender(row['Q100'], json_dict2))
                
            if (row['Q102']):
                json_dict['CUSTOMFIELDS'].append(getEthnicity(row['Q102'], json_dict2))

            # Section 7: UCI Affiliation
            if row['UCI Affiliation']:
                uci_affiliation = row['UCI Affiliation'].split(",")
                json_dict['CUSTOMFIELDS'].extend(getUCIAffiliation(uci_affiliation, json_dict2))
                # affiliationList = getUCIAffiliation(uci_affiliation,json_dict2) #list(Dictionary) -> add dictionary into json_dict['CUSTOMFIELDS']
                # for indx, i in enumerate(affiliationList):
                #     json_dict['CUSTOMFIELDS'].append(indx, i)
                
            academic_area = []
            if (row['UCI Student']):
                academic_area.extend(row['UCI Student'].split(","))
            if (row['UCI Alumni']):
                academic_area.extend(row['UCI Alumni'].split(","))
            if (row['UCI Faculty']):
                academic_area.extend(row['UCI Faculty'].split(","))
            if (academic_area):
                academic_area = list(set(academic_area))  # remove duplicated
                json_dict['CUSTOMFIELDS'].append(academicDecoder(academic_area, json_dict2))

            if (row['UCI Staff_1_TEXT'] or row['UCI Staff_2_TEXT']):
                uci_staff_str = row['UCI Staff_1_TEXT'] + row['UCI Staff_2_TEXT']
                json_dict['CUSTOMFIELDS'].append(getUCIStaff(uci_staff_str, json_dict2))

            # Transfer CSV data into Insightly
            print(json_dict)
            r = requests.post(insightlyAPIurl + '/Contacts', json=json_dict, auth=(insightlyAPIkey.getAPI(), ''))
            if r.status_code != 200:
                logObject.writePostFailure(rownum, r.status_code)
            else:
                logObject.writePostSuccess(rownum)
            imported_count += 1

            # Close savedData file
            with open("savedData.txt", "w+") as file:
                file.write(datetime.strftime(date_time_obj, '%Y-%m-%d %H:%M:%S'))
                file.close()

            # print(imported_count, "row(s) of data has been transferred successfully.")


    except (csv.Error, FileNotFoundError) as e:  # display error
        if type(e) is FileNotFoundError:
            message = "The file inputted into the program can not be found within the path"
        else:
            message = "There has been a CSV error"
        logObject.writeError(rownum, e, message)

    return message, imported_count

def saveDate(date):
    with open("savedData.txt", "w+") as file:
        file.write(date)
        file.close()