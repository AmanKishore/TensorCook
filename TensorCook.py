
from google_images_download import google_images_download

food_list = ['food with protein','unhealthy food','carbs','food with sugar','vegetables']

for food in food_list:
    args = {"keywords":food, "format": "jpg", "limit":1000, "output_directory":"./tf_files/food_images"}
    response = google_images_download.googleimagesdownload()
    paths = response.download(args)