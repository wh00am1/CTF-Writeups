# CTFLearn Writeup (難度:easy)

## 分類
[Web](#Web)

[Forensics](#Forensics)

[Misc](#Misc)

[Programming](#Programming)

## Web

### Basic Injection
題目給出一個網頁，內含搜尋功能，推測為SQL injection

先試試萬用密碼:`' OR '1' = '1`

在 `Name: fl4g__giv3r` 處找到flag

(web就到此結束了QQ)

## Forensics

### 水題

`Forensics 101`, `Taking LS`, `WOW.... So Meta`


熟悉基本命令即可得解

### Binwalk
此題為圖片隱寫，用binwalk(`dd` 提取全部)即可從 `PurpleThing.jpeg` 提取有flag的png檔

### A CAPture of a Flag
給出flag.pcap，一開始以為是follow stream, 但udp stream似乎沒有flag

轉而尋找流量也很大的http，果然在第247個封包找到一串不尋常的字串: `ZmxhZ3tBRmxhZ0luUENBUH0=`

經base64解碼後得到flag

## Misc

### 水題

`Where Can My Robot Go?`, `Practice Flag`, `Reversal of fortune` 都是

### Wikipedia
題目給出一個IP地址(128.125.52.138)，以及 `Wikipedia` 兩個線索

but解不出來 QQ

後來看別人解才知道，搜尋flag頁面的編輯史，128.125.52.138曾更改過

可以在 https://en.wikipedia.org/w/index.php?oldid=676540540 找到 flag

### QR Code
使用[線上QRCode工具](https://webqr.com/index.html)解碼

得到字串，但並不是base64，而是rot13

### QR Code v2
一樣使用[線上QRCode工具](https://webqr.com/index.html)解碼

拿到url: `https://mega.nz/#!9NFhUbwQ!vtrLVum8z-ZXzur33RrGJ4uivMJhA9_5TW2ulHucXoU`

進去之後，下載Flag.txt

### IP Tracer
題目給出一個IP位址(159.167.16.5)，而且說 "find where the IP Address is located"

使用[線上IP地址定位工具](https://www.iplocation.net/)

不是 `Warwick`, 是 `London`

## Programming

### Simple Programming
題目說:

"I need to know how many lines there are where the number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2."

並給出一個副檔

根據題意，寫一個Python檔算出有幾行的0是三的倍數，1是2的倍數

詳見[附檔](https://github.com/wh00am1/CTF-Writeups/blob/master/ctflearn.com/easy/easy.py)

解出行數為6662

## Crypto

### 水題
`Character Encoding`, `Hextroadinary`, `Base 2 2 the 6`, `Vigenere Cipher`, `Reverse Polarity`, `Morse code`

### BruXOR
根據題意(暴力破解xor)，用 `xortool` 得解 (`xortool -x -b`)

### HyperStream Test #2
這題是一種特殊的加密法(Bacon Cipher)，只使用了A和B

使用[線上工具](https://www.dcode.fr/bacon-cipher)轉換得解



###### 小小心得

`dcode.fr` 真的好用