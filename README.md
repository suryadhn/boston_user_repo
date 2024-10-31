# boston_user_repo
*********************************************************************************************************************************************************************************
**An explanation of how I scraped the data**:
Using python code and using generated token I scraped data. Initially faced limit issues which was later overcome by pagination and used pause (sleep(1)) to avoid hitting rate limits.
*********************************************************************************************************************************************************************************
**The most interesting and surprising fact I found after analyzing the data**:
Length of developer's bio negatively impacts number of followers. Regression slope of followers on bio word count is -3.082 which means on average, for each additional word in developer’s bio, number of followers decreases by about 3.082 followers.
*********************************************************************************************************************************************************************************
**An actionable recommendation for developers based on my analysis**:
Write short and precise bio. Python, JavaScript are popular recently. Be active on git, follow more people as hireable users follow about 112 more people than users who are not marked as hireable.
*********************************************************************************************************************************************************************************
