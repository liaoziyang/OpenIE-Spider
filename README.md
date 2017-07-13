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

Copy code into local.

```
git clone git@github.com:liaoziyang/Stanford-OpenIE-Spider.git
cd Stanford-OpenIE-Spider
```


