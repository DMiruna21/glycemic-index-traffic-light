# GLYCEMIC INDEX TRAFFIC LIGHT 
> ** Disclaimer** educational project, it doesn't have a medical purpose!

## What it does
The program analyzes the given photo, recognizes the food using a pretrained model (nateraw/food, Hugging Face, trained on Food-101),so that then it'll give a result based on the GI:
- Low GI: 55 or less (green)
- Medium GI: 56 - 69 (yellow)
- High GI: 70 or more (red)

## How it works
- A pretrained image classification model (trained on Food-101) recognizes the food in the photo.
- The recognized food is looked up in food_categories.csv, which stores its glycemic index (GI).
- The GI is mapped to a traffic light category: green (≤ 55), yellow (56–69) or red (≥ 70).

## How to run
To get the result that we want, we will write in terminal: python recognize_food.py photo.jpg.
  ```bash
  python recognize_food.py photo.jpg
  ```

## Next steps
Fine-tuning for Romanian food, a web interface and API.

## Credits
University of Sydney (glycemicindex.com), Food-101, nateraw/food(Hugging Face)

## Limitations
The glycemic index is an approximation; mixed dishes vary by recipe; the lookup table currently covers only a few foods.