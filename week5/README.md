# assignment
1-  
INSERT INTO `website`.`user`(`username`,`password`) VALUES('ply','ply');
INSERT INTO `website`.`user`(`username`,`password`) VALUES('ply2','ply2');
INSERT INTO `website`.`user`(`username`,`password`) VALUES('ply3','ply3');
INSERT INTO `website`.`user`(`username`,`password`) VALUES('ply4','ply4');
INSERT INTO `website`.`user`(`username`,`password`) VALUES('ply5','ply5');

![image](https://user-images.githubusercontent.com/73087725/111946843-44389680-8b17-11eb-8607-d7198ac4abdf.png)


2-
SELECT * FROM `website`.`user`;

![image](https://user-images.githubusercontent.com/73087725/111946875-531f4900-8b17-11eb-8152-786ee47f4c99.png)


3-
SELECT COUNT(*) FROM `website`.`user`;

![image](https://user-images.githubusercontent.com/73087725/111946695-f0c64880-8b16-11eb-99f4-d10669bad80b.png)


4-
SELECT * FROM `website`.`user` 
ORDER BY `time` DESC;

![image](https://user-images.githubusercontent.com/73087725/111947359-464f2500-8b18-11eb-9a3d-a632441cca8e.png)


5-
SELECT * FROM `website`.`user` 
WHERE `id`=2 OR `id`=3 OR `id`=4 
ORDER BY `time` DESC;

![image](https://user-images.githubusercontent.com/73087725/111947797-13596100-8b19-11eb-9795-0edb73f29c4c.png)


6-
SELECT * FROM `website`.`user` WHERE `username`='ply' ;

![image](https://user-images.githubusercontent.com/73087725/111948060-8367e700-8b19-11eb-868e-53877734d92f.png)


7-
SELECT * FROM `website`.`user` WHERE `username`='ply' AND `password`='ply';

![image](https://user-images.githubusercontent.com/73087725/111948237-d346ae00-8b19-11eb-9451-7c5c0b968cfc.png)


8-
UPDATE `website`.`user` SET `name`='丁滿' WHERE `username`='ply';

![image](https://user-images.githubusercontent.com/73087725/111948627-68e23d80-8b1a-11eb-87f0-5da2bbc6ba80.png)
![image](https://user-images.githubusercontent.com/73087725/111948686-80212b00-8b1a-11eb-9b8c-eacea06cb6e6.png)


9-
DELETE  FROM `website`.`user`;

![image](https://user-images.githubusercontent.com/73087725/111949073-09d0f880-8b1b-11eb-88df-361c75f90f0e.png)



