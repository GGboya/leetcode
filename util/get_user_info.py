import http.client
import json
def GetLastSubmissionTime(ip):
    conn = http.client.HTTPSConnection("leetcode.cn")
    payload = json.dumps({
        "query": "\n    query recentAcSubmissions($userSlug: String!) {\n  recentACSubmissions(userSlug: $userSlug) {\n    submissionId\n    submitTime\n    question {\n      translatedTitle\n      titleSlug\n      questionFrontendId\n    }\n  }\n}\n    ",
        "variables": {
            "userSlug": ip
        }
    })

    payload_rank = json.dumps({
        "query":
            "\n    query userContestRankingInfo($userSlug: String!) {\n  userContestRanking(userSlug: $userSlug) {\n    attendedContestsCount\n    rating\n    globalRanking\n    localRanking\n    globalTotalParticipants\n    localTotalParticipants\n    topPercentage\n  }\n  userContestRankingHistory(userSlug: $userSlug) {\n    attended\n    totalProblems\n    trendingDirection\n    finishTimeInSeconds\n    rating\n    score\n    ranking\n    contest {\n      title\n      titleCn\n      startTime\n    }\n  }\n}\n    ",
        "variables": {
            "userSlug": ip
        }
    })

    payload_solve = json.dumps({
        "query":
            "\n    query userQuestionProgress($userSlug: String!) {\n  userProfileUserQuestionProgress(userSlug: $userSlug) {\n    numAcceptedQuestions {\n      difficulty\n      count\n    }\n    numFailedQuestions {\n      difficulty\n      count\n    }\n    numUntouchedQuestions {\n      difficulty\n      count\n    }\n  }\n}\n    ",
        "variables": {
            "userSlug": ip
        }
    })

    payload_user = json.dumps({
        "query": "\n    query userProfilePublicProfile($userSlug: String!) {\n  userProfilePublicProfile(userSlug: $userSlug) {\n    haveFollowed\n    siteRanking\n    profile {\n      userSlug\n      realName\n      aboutMe\n      asciiCode\n      userAvatar\n      gender\n      websites\n      skillTags\n      ipRegion\n      birthday\n      location\n      useDefaultAvatar\n      github\n      school: schoolV2 {\n        schoolId\n        logo\n        name\n      }\n      company: companyV2 {\n        id\n        logo\n        name\n      }\n      job\n      globalLocation {\n        country\n        province\n        city\n        overseasCity\n      }\n      socialAccounts {\n        provider\n        profileUrl\n      }\n      skillSet {\n        langLevels {\n          langName\n          langVerboseName\n          level\n        }\n        topics {\n          slug\n          name\n          translatedName\n        }\n        topicAreaScores {\n          score\n          topicArea {\n            name\n            slug\n          }\n        }\n      }\n    }\n    educationRecordList {\n      unverifiedOrganizationName\n    }\n    occupationRecordList {\n      unverifiedOrganizationName\n      jobTitle\n    }\n  }\n}\n    ",
        "variables": {
            "userSlug": ip
        }
    })


    headers = {
        'authority': 'leetcode.cn',
        'authorization': '',
        'cookie': '_bl_uid=32lgt5Iq4estR4ovpv48fej2UI58; gr_user_id=9cd64ed3-db69-4693-b361-a68ed8316706; csrftoken=PPT5fcdFRpPnRbcHzNYbBhwpTv1HxSKtrqyurg4uKxuW0aBUPMTLb0Cu5LwyCmm6; a2873925c34ecbd2_gr_last_sent_cs1=sanxiconze-2; _ga=GA1.2.827755954.1656827815; aliyungf_tc=3f88358c46c63b3cf747bfa7f9c952beb3e2cc9b91a526c574c455d381d3d562; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1656848229; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1656827815,1656848229; a2873925c34ecbd2_gr_session_id=0f3c7ce7-f057-4e09-9e0d-d8b006ba0375; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=0f3c7ce7-f057-4e09-9e0d-d8b006ba0375; a2873925c34ecbd2_gr_session_id_0f3c7ce7-f057-4e09-9e0d-d8b006ba0375=true; a2873925c34ecbd2_gr_cs1=sanxiconze-2; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMzk3NjA5IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiN2RiZjJiMjI5ZDZiMmQ0MWI0ZTMzOTVlYmExMTE5YzI2ZGI0M2Q1ZTE1M2FkNjI1YmJmNDVkYzEwNWI1OWFjMSIsImlkIjozOTc2MDksImVtYWlsIjoic2FueGljb256ZUBnbWFpbC5jb20iLCJ1c2VybmFtZSI6InNhbnhpY29uemUtMiIsInVzZXJfc2x1ZyI6InNhbnhpY29uemUtMiIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNuL2FsaXl1bi1sYy11cGxvYWQvZGVmYXVsdF9hdmF0YXIucG5nIiwicGhvbmVfdmVyaWZpZWQiOnRydWUsIl90aW1lc3RhbXAiOjE2NTY4MjMxNTkuOTk4MTUzNywiZXhwaXJlZF90aW1lXyI6MTY1OTM4MDQwMCwidmVyc2lvbl9rZXlfIjowLCJsYXRlc3RfdGltZXN0YW1wXyI6MTY1Njk0MDY3MX0.-8yAB0-g6Vt2xFGdvuO5HxkV9TSHAywGzeD-Ea2fhE8',
        'x-csrftoken': 'PPT5fcdFRpPnRbcHzNYbBhwpTv1HxSKtrqyurg4uKxuW0aBUPMTLb0Cu5LwyCmm6',
        'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)',
        'content-type': 'application/json'
    }

    conn.request("POST", "/graphql/noj-go/", payload_rank, headers)
    res = conn.getresponse()
    data = res.read()
    dictStr = json.loads(data.decode("utf-8"))
    try:
        user_rank = int(dictStr["data"]["userContestRanking"]["rating"])
    except (IndexError, TypeError):
        user_rank = -1

    conn.request("POST", "/graphql/noj-go/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    s = data.decode("utf-8")
    idx = s.find("submitTime")
    if idx == -1:
        return -1, user_rank, 0, 0
    last_time = int(s[idx + 12: idx + 22])

    conn.request("POST", "/graphql/", payload_solve, headers)
    res = conn.getresponse()
    data = res.read()
    dictStr = json.loads(data.decode("utf-8"))
    try:
        user_solve_easy = int(dictStr["data"]["userProfileUserQuestionProgress"]["numAcceptedQuestions"][0]["count"])
    except IndexError:
        user_solve_easy = 0
    try:
        user_solve_medi = int(dictStr["data"]["userProfileUserQuestionProgress"]["numAcceptedQuestions"][1]["count"])
    except IndexError:
        user_solve_medi = 0
    try:
        user_solve_hard = int(dictStr["data"]["userProfileUserQuestionProgress"]["numAcceptedQuestions"][2]["count"])
    except IndexError:
        user_solve_hard = 0

    cnt = user_solve_easy+user_solve_hard+user_solve_medi

    conn.request("POST", "/graphql/", payload_user, headers)
    res = conn.getresponse()
    data = res.read()
    dictStr = json.loads(data.decode("utf-8"))
    username = dictStr['data']['userProfilePublicProfile']['profile']['realName']

    return last_time, user_rank, cnt, username