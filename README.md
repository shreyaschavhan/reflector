<img src=https://user-images.githubusercontent.com/68887544/182011989-f9026ec6-4286-4d8b-bc26-c43dcf0643e9.png width=150px align=left>

`Shreyas Chavhan`


## ⁍ 𝐑𝐞𝐟𝐥𝐞𝐜𝐭𝐨𝐫 - 𝐂𝐡𝐞𝐜𝐤 𝐆𝐞𝐭 𝐏𝐚𝐫𝐚𝐦𝐞𝐭𝐞𝐫 𝐑𝐞𝐟𝐥𝐞𝐜𝐭𝐢𝐨𝐧 𝐢𝐧 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞

Reflector is a simple python3 script to automate the process of finding reflected get parameters to simplify reflected XSS finding process for personal use.


## ⁍ 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐚𝐭𝐢𝐨𝐧

- Installation:
```
git clone https://github.com/shreyaschavhan/reflector
```

- Dependencies
```
pip install requests
```

## ⁍ 𝐔𝐬𝐚𝐠𝐞

```
python reflector.py file.txt
```

- where `file.txt` is any file with a list of urls with GET parameters
 
## ⁍ 𝐍𝐨𝐭𝐞𝐬

- This script was created for personal use.
- The script uses `"xssteststring"` as a test string by default to check for the reflection. Feel free to use your own string.
- Output of the script is stored at `./output.txt`
- Output contains all urls with parameters that reflects `xssteststring` in it's response.

## ⁍ 𝐄𝐱𝐚𝐦𝐩𝐥𝐞

- `file.txt`
```
https://brutelogic.com.br/gym.php?p00=hello
https://brutelogic.com.br/gym.php?p01=hello
https://brutelogic.com.br/gym.php?p02=hello
https://brutelogic.com.br/gym.php?p03=hello
https://brutelogic.com.br/gym.php?p04=hello
https://brutelogic.com.br/gym.php?p05=hello
https://brutelogic.com.br/gym.php?p06=hello
https://brutelogic.com.br/gym.php?p07=hello
https://brutelogic.com.br/gym.php?p08=hello
https://brutelogic.com.br/gym.php?p09=hello
https://brutelogic.com.br/gym.php?p10=hello
https://brutelogic.com.br/gym.php?p11=hello
https://brutelogic.com.br/gym.php?p12=hello
https://brutelogic.com.br/gym.php?p13=hello
https://brutelogic.com.br/gym.php?p14=hello
https://brutelogic.com.br/gym.php?p15=hello
https://brutelogic.com.br/gym.php?p16=hello
https://brutelogic.com.br/gym.php?p17=hello
https://brutelogic.com.br/gym.php?p18=hello
https://brutelogic.com.br/gym.php?p19=hello
https://brutelogic.com.br/gym.php?p20=hello
https://brutelogic.com.br/gym.php?p21=hello
https://brutelogic.com.br/gym.php?p22=hello
https://brutelogic.com.br/gym.php?p23=hello
https://brutelogic.com.br/gym.php?p24=hello
https://brutelogic.com.br/gym.php?p25=hello
https://brutelogic.com.br/gym.php?p26=hello
https://brutelogic.com.br/gym.php?p27=hello
https://brutelogic.com.br/gym.php?p28=hello
https://brutelogic.com.br/gym.php?p29=hello
https://brutelogic.com.br/gym.php?p30=hello
https://brutelogic.com.br/gym.php?p31=hello
https://brutelogic.com.br/gym.php?p32=hello
https://brutelogic.com.br/gym.php?p33=hello
https://brutelogic.com.br/gym.php?p34=hello
```

- Output:

![image](https://user-images.githubusercontent.com/68887544/182012516-1e8e6334-a43a-4296-92d7-7d8285252dd6.png)

- `output.txt`

```
https://brutelogic.com.br/gym.php?p01=xssteststring
https://brutelogic.com.br/gym.php?p02=xssteststring
https://brutelogic.com.br/gym.php?p03=xssteststring
https://brutelogic.com.br/gym.php?p04=xssteststring
https://brutelogic.com.br/gym.php?p05=xssteststring
https://brutelogic.com.br/gym.php?p06=xssteststring
https://brutelogic.com.br/gym.php?p07=xssteststring
https://brutelogic.com.br/gym.php?p08=xssteststring
https://brutelogic.com.br/gym.php?p09=xssteststring
https://brutelogic.com.br/gym.php?p10=xssteststring
https://brutelogic.com.br/gym.php?p11=xssteststring
https://brutelogic.com.br/gym.php?p12=xssteststring
https://brutelogic.com.br/gym.php?p13=xssteststring
https://brutelogic.com.br/gym.php?p14=xssteststring
https://brutelogic.com.br/gym.php?p15=xssteststring
https://brutelogic.com.br/gym.php?p16=xssteststring
https://brutelogic.com.br/gym.php?p17=xssteststring
https://brutelogic.com.br/gym.php?p18=xssteststring
https://brutelogic.com.br/gym.php?p19=xssteststring
https://brutelogic.com.br/gym.php?p20=xssteststring
https://brutelogic.com.br/gym.php?p22=xssteststring
https://brutelogic.com.br/gym.php?p23=xssteststring
https://brutelogic.com.br/gym.php?p24=xssteststring
https://brutelogic.com.br/gym.php?p28=xssteststring
https://brutelogic.com.br/gym.php?p30=xssteststring
```

`~ By Shreyas Chavhan`
