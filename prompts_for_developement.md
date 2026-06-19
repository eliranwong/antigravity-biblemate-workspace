# Prompts for Development

## Prompt for Creating Bible Skill and /bible Command

```
Create a new skill and a new slash command / workflow, to retrieve bible verses:

skill name should be simply bible

slash command should be simply /bible

bible databases are in sqlite format, stored either in ~/biblemate/data/bibles or ~/biblemate/data_custom/bibles

Remember use home variable instead of hardcoding absolute paths, to make this repository portable.

Valid bible database filenames are ended with *.bible

retrieve from table `Verses`

NET.bible is the default bible if no bible version is specified

the command `/bible` can take both bible version(s) and bible reference(s)

if bible version is not specified, NET.bible is the default database for retrieval.  If a specified version, use that version, If more than one version is specified, all specified versions are retrieved with each verse display line by line comparison of the specified versions.

bible references can be single or multiple verse(s), e.g. John 3:16-18; Rm 5-8

bible references can also be a chapter a verse or multiple verse range

examples for use: 

/bible John 3:16 # use NET.bible as default

/bible John 3 # retrieve the whole chapter from the first verse to the last

/bible John 3:16-18; Deut 6:4; Rom 5-8 # retrieve multiple verses from different books.

/bible CUV John 3:16-18 # use CUV.bible as it is specified

/bible NET CUV John 3:16-18 # compare NET CUV every single verse, line by line, from John 3:16 to 3:18

make sure you don't hardcode bible version list available in ~/biblemate/data/bibles and ~/biblemate/data_custom/bibles , as users can dynamatically add or remove bible databases into or from this folder.  Instead of hardcoding a static bible version list, you should always check if bible version specified is a valid name in those folder.
```



## Prompt for Creating Commentary Skill and /commentary Command

```
Now, along a similar line, create a new skill and a new slash command workflow, to retrieve bible commentary:

skill name should be simply `commentary`

slash command should be simply `/commentary`

commentaries are in sqlite format, stored either in `~/biblemate/data/commentaries` or `~/biblemate/data_custom/commentaries`

Note: make sure you don't hardcode commentary version list available in `~/biblemate/data/commentaries` and `~/biblemate/data_custom/commentaries` , because users can dynamatically add or remove commentary databases into or from this folder.  Instead of hardcoding a static commentary version list, you should always check if commentary version specified is a valid name in those folder.

Remember use home variable instead of hardcoding absolute paths, to make this repository portable.

Valid commentary filenames are formatted like `c<commentary_version>.commentary`, so each commentary filename starts with `c` followed by the commentary version abbreviation, then `.commentary`. for example:
`cAIC.commentary`, `cBI.commentary`, etc. and each is its own commentary database.

retrieve from table `Commentary`, the `Scripture` column contains the commentary text content that is intended to be retrieved. 

Note: there may be a challenge for you, some Commentary table, like the one in `cAIC.commentary` contains Book, Chapter, and Verse entries, but most of the others have Book, Chapter entries only.  In the latter case, the `Scripture` column contains the commentary text content for the whole chapter.  You need a further step to retrieve only the relevant verses/verse range sections from the commentary text content, based on the given verse range.  For example, if verse range is John 3:16-18, and the commentary text content is for the whole chapter, you need to retrieve only the sections relevant to John 3:16-18.  You should use text processing, and natural language understanding techniques to achieve this goal or any better alternatives.

`cAIC.commentary` is the default commentary if no commentary version is specified

the command `/commentary` can take both commentary version(s) and bible reference(s)

if commentary version is not specified, `cAIC.commentary` is the default database for retrieval.  If a specified version, use that version, If more than one version is specified, all specified versions are retrieved for comparison for each given bible reference.

bible references can be single or multiple verse(s), e.g. John 3:16-18; Rm 5-8

bible references can also be a chapter a verse or multiple verse range

examples for use: 

/commentary John 3:16 # use `cAIC.commentary` as default

/commentary John 3 # retrieve the whole chapter from the first verse to the last

/commentary John 3:16-18; Deut 6:4; Rom 5-8 # retrieve multiple commentaries for the given verses from different books.

/commentary BI John 3:16-18 # use `cBI.commentary` as it is specified

/commentary AIC BI John 3:16-18 # compare `cAIC.commentary` and `cBI.commentary` for the given bible references
```