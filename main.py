from google_play_scraper import Sort, reviews, reviews_all
import pandas as pd

app_id = 'com.invest.bamboo'

result, continuation_token = reviews(
    app_id,
    lang='en',
    country='us',
    sort=Sort.RATING,
    count=189,
    filter_score_with=None
)

data = pd.DataFrame(result)
data = data[['content', 'score']]

data.to_csv('bamboo_reviewsss.csv', index=False)
print('Reviews saved!')
