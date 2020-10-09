# Bash Challenges

## The Locked Chest
* mkdir secret_chamber
* touch secret_chamber/chest
* echo treasure > secret_chamber/chest
* chmod -rw secret_chamber/chest
* mv secret_chamber .secret_chamber
* sudo cat .secret_chamber/chest

## Spices

* mkdir fruit
* cd fruit
* touch apple banana cherry pear mango raspberry lemon
* cd ..
* ls fruit > fruits.txt
* cd fruit
* ls -1 *a* > ../fruitswitha.txt
* cd ..
* diff fruits.txt fruitswitha.txt

## Bash Scripting

* touch hello.sh
* vim hello.sh
 * press i
```
#!/bin/bash
echo "Hello World"
```
 * press esc
 * press :wq

* chmod +x hello.sh
* source hello.sh
* vim hello.sh
 * press i
```
#!/bin/bash
echo $1
```
 * press esc
 * press :wq
* source hello.sh 'Hello World'
* touch hello10.sh
* vim hello10.sh
 * press i
```
#!/bin/bash
source hello.sh "hello"
source hello.sh "this"
source hello.sh "is"
source hello.sh "script"
source hello.sh "!"
source hello.sh "new"
source hello.sh "script"
source hello.sh "who"
source hello.sh "dis"
source hello.sh "?"
```
 * press esc
 * press :wq
* chmod +x hello10.sh
* ./hello10.sh
