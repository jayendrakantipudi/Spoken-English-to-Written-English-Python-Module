# Spoken English to Written English
A python module that converts spoken english to written english.

# Installation
Please ensure that you have updated pip3 to the latest version before installing spr2wrt.

You can install the module using Python Package Index using the below command.

>> python3 setup.py install

# Features Implemented:
### Conversion Types

1.Make Repetitions (conversion_type='make_repetitions')

  Ex:  Triple A --> AAA **OR** three hundred fity two times A --> *gives 352 times a*

2.Convert English Numbers to Numericals (conversion_type='spoken_to_written_numbers')

  Ex:  one hundred forty two--> 142 **OR**  two hundred thousand five hundred forty two --> 200542

3.Convert Spoken English to Written English (conversion_type='spoken_to_written_english')

  Ex:  i have two thousand fifty six dollars with me.-->i have $2056 with me. **OR**  hastag sports --> #sports

# To be implemented
These are converted individually i.e., by mentioning the conversion type of any one of the above three.For converting a whole paragraph, we need to classify the sentences of each paragraph into one of the above conversion types.

# Instructions to use:
(in python)

*Type1*
>>from spk2wrt import spk2wrt

>>a = spk2wrt.conversionSystem('double A')

>>print(a.convert_to_written(conversion_type='make_repetitions'))

   *returns the converted string*

*Type2*
>>from spk2wrt import spk2wrt

>>a = spk2wrt.conversionSystem('twenty five thousand sixty six hundred')

>>print(a.convert_to_written(conversion_type='spoken_to_written_numbers'))

   *returns the converted number*

*Type3*
>>from spk2wrt import spk2wrt

>>a = spk2wrt.conversionSystem('i have twenty five thousand sixty six hundred dollars with me.')

>>print(a.convert_to_written(conversion_type='spoken_to_written_english'))

   *returns the converted string*
