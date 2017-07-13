# Stanford-OpenIE-Spider
Extract Information from WebCorpus using Stanford Open Information Extraction.

## About Stanford IE

Open information extraction (open IE) refers to the extraction of structured relation triples from plain text, such that the schema for these relations does not need to be specified in advance. For example, Barack Obama was born in Hawaii would create a triple (Barack Obama; was born in; Hawaii), corresponding to the open domain relation "was born in". This software is a Java implementation of an open IE system as described in the paper:

Gabor Angeli, Melvin Johnson Premkumar, and Christopher D. Manning. Leveraging Linguistic Structure For Open Domain Information Extraction. In Proceedings of the Association of Computational Linguistics (ACL), 2015. The system first splits each sentence into a set of entailed clauses. Each clause is then maximally shortened, producing a set of entailed shorter sentence fragments. These fragments are then segmented into OpenIE triples, and output by the system.

More information can be found here : http://nlp.stanford.edu/software/openie.html

## About Open Information Extraction(http://openie.allenai.org/)

This is a web service that implement information extraction feature from web corpus using Stanford IE. We can search the relation in the web from this website.

## Usage

First of all, please make sure python is installed.

```
python --version
```

Install scrapy. 

```
sudo pip install scrapy
```
You can also see the offical document from here. https://doc.scrapy.org/en/latest/intro/install.html

Install beautifulsoup4.
```
sudo pip install beautifulsoup4
```

Copy code into local.

```
git clone git@github.com:liaoziyang/Stanford-OpenIE-Spider.git
cd Stanford-OpenIE-Spider
```

### Argument

Require at least one parameter below, using `-a` option.

- `arg1`: Noun in the left side of the relationship. Default null.
- `rel`: The relationship. Default null.
- `arg2`: Noun in the right side of the relationship. Default null.

And you can write the result into file by using `-o` option.

### Example

Extract the information "What kills bacteria?" from the web corpus.

```
scrapy runspider -a rel=kills -a args2=bacteria openie_spider.py -o result.json
```
And the result in `result.json` is like:
`key` is the string representation of the result and the `value` is the frequency of the result appeared in the web corpus.

```json
[
{"Antibiotic": 165},
{"Chlorine": 76},
{"Water": 59},
{"Benzoyl peroxide": 45},
{"Heat": 40},
{"Antiseptic": 38},
{"Pasteurization": 35},
{"Cooking": 34},
{"Vinegar": 34},
{"Honey": 28},
{"Tea tree oil": 24},
{"Ultraviolet": 24},
{"Alcohol": 24},
{"The process": 21},
{"This drug": 21},
{"the oil": 19},
{"the skin": 17},
{"Food": 16},
{"chemicals": 15},
{"Cell (biology)": 14},
{"Isoniazid": 2},
{"sebum production": 2},
{"the UV light feature": 2},
{"Lidocaine": 2},
{"Patent-pending germicidal chamber": 2},
{"Titanium dioxide": 2},
{"shedding": 2},
{"Gut flora": 2},
{"six antiseptic agents": 2},
{"The warm salt water": 2},
{"Chlorhexidine": 2},
{"bitter component": 2},
{"a small anti-microbial bomb": 2},
{"an herb": 2},
{"Cotton": 2},
{"a day": 2},
{"the microwave": 2},
{"cancer cells": 2},
{"Food irradiation": 2},
{"Virus": 2},
{"Studies": 2},
{"Polymer": 2},
{"Active ingredient": 2},
{"Electron": 2},
{"Freezing": 2},
{"Fahrenheit": 2},
{"These peptides": 2},
{"Clarithromycin": 2},
{"redness": 2},
{"Saltwater": 2},
{"BP": 2},
{"White blood cell": 2},
{"a salve": 2},
{"the soap": 2},
{"Spice": 2},
{"Egg (food)": 2},
{"most toiletries": 2},
{"both": 2},
{"Neem": 2},
{"a role": 2},
{"Chamomile": 2},
{"Clindamycin": 2},
{"the formation": 2},
{"humans": 2},
{"three minutes": 2},
{"Sparfloxacin": 2},
{"one minute": 2},
{"Burning": 2},
{"High heat": 2},
{"A sanitizer test kit": 2},
{"Air purifier": 2},
{"the teeth and gums": 2},
{"Intestine": 2},
{"Concentration": 2},
{"Juice": 2},
{"Your goal": 2},
{"Sodium": 2},
{"Zinc": 2},
{"The face": 3},
{"Swimming pool": 3},
{"Vancomycin": 3},
{"Alcoholic beverage": 3},
{"Urine": 3},
{"Nitric oxide": 3},
{"Fever": 3},
{"This combination": 3},
{"The wine": 3},
{"the heart": 3},
{"Electricity": 3},
{"lemon": 3},
{"soothes": 3},
{"Phagocyte": 3},
{"devices": 3},
{"The Aprilaire 5000 Air Cleaner": 3},
{"Tanning bed": 2},
{"dirt and dust": 2},
{"These rinses": 2},
{"This medication": 2},
{"Bacteriophage": 3},
{"Toothpaste": 3},
{"chemicals and particles": 3},
{"Cell wall": 3},
{"Amoxicillin": 3},
{"Blood pressure": 3},
{"Miphil": 3},
{"Roasting": 3},
{"plaque": 3},
{"all": 3},
{"the tight-lidded pot": 3},
{"UV germicidal light": 3},
{"The idea": 3},
{"Azelaic acid": 3},
{"energy": 3},
{"Sulfur": 3},
{"Ammonium hydroxide": 3},
{"The purpose": 3},
{"these beds": 3},
{"160 degrees": 3},
{"Tea": 4},
{"Macrophage": 4},
{"Apple cider vinegar": 4},
{"Sodium bicarbonate": 4},
{"Additives": 4},
{"Acne vulgaris": 4},
{"Stomach": 4},
{"Antibacterial soap": 4},
{"Citric acid": 4},
{"15 seconds": 4},
{"Infection": 4},
{"Iodine": 4},
{"Disinfectant": 4},
{"Bactericidal antibiotics": 4},
{"Coconut oil": 4},
{"the same time": 4},
{"formula": 4},
{"Levofloxacin": 4},
{"The Lampe Berger": 4},
{"Nanoparticle": 3},
{"Saliva": 6},
{"Ion": 6},
{"the acidity": 6},
{"Odor": 6},
{"your body": 5},
{"Acai": 5},
{"Hair": 5},
{"Protein": 5},
{"Meat": 5},
{"Cabbage": 5},
{"Clothes dryer": 5},
{"Sebaceous gland": 5},
{"Lemon juice": 5},
{"Laser": 5},
{"Water filter": 5},
{"Wound": 5},
{"action": 5},
{"Antimicrobial": 4},
{"Antibody": 4},
{"Aloe": 4},
{"Immune system": 9},
{"Inflammation": 9},
{"Ingredient": 8},
{"Bactericide": 8},
{"Toxin": 8},
{"These medicines": 8},
{"Tap water": 8},
{"Neutrophil granulocyte": 7},
{"Salicylic acid": 7},
{"Colloidal silver": 7},
{"the treatment": 6},
{"Sunlight": 6},
{"Copper": 6},
{"Two-week triple therapy": 6},
{"Essential oil": 6},
{"Chemotherapy": 6},
{"the solution": 6},
{"Penicillin": 6},
{"Radical (chemistry)": 6},
{"Hydrogen peroxide": 6},
{"the sun": 14},
{"Oxygen": 14},
{"the light": 14},
{"the product": 14},
{"Irradiation": 12},
{"pores": 12},
{"Salt": 12},
{"Bleach (manga)": 11},
{"Temperature": 11},
{"Silver": 11},
{"NOT": 11},
{"the ability": 11},
{"Ozone": 11},
{"Milk": 10},
{"Bleach": 10},
{"Garlic": 9},
{"the growth": 9},
{"numerous active agents": 9},
{"Boiling": 9},
{"the steam": 9}
]
```

