# 要求三:SQL CRUD
* 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。

![](/week-5/img/insertMember.png)
檢查
![](/week-5/img/checkInsertMember.png)

* 使用 SELECT 指令取得所有在 member 資料表中的會員資料。

![](/week-5/img/checkAllMember.png)

* 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。

![](/week-5/img/sortAllMember.png)

* 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，
由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )。

![](/week-5/img/get2-4Member.png)

* 使用 SELECT 指令取得欄位 username 是 test 的會員資料。

![](/week-5/img/getUsernameTest.png)

* 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

![](/week-5/img/checkUsernameAndPassword.png)

* 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改
成 test2。

safe_update
![](/week-5/img/safe_update.png)
改名
![](/week-5/img/renametest.png)

# 要求四:SQL Aggregate Functions
* 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。

![](/week-5/img/count%20rows.png)

* 取得 member 資料表中，所有會員 follower_count 欄位的總和。

![](/week-5/img/checkMemberSumandAvg.png)

* 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

![](/week-5/img/checkMemberSumandAvg.png)

# 要求五
* 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。

![](/week-5/img/joinAll.png)

* 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。

![](/week-5/img/jointest.png)

* 使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。

![](/week-5/img/joinavg.png)

* 使用FOREIGN KEY

![](/week-5/img/foreignkey.png)