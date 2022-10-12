<h1 align="center">
	<img alt="aitBnB" src="https://cdn.icon-icons.com/icons2/836/PNG/512/Airbnb_icon-icons.com_66791.png" height="30"/> AirBnB clone - The console
</h1>
<p align="center">
	<b><i>HOLBERTON SCHOOL AirBnB clone - The console</i></b><br>
</p>
<p align="center">
	<img alt="HBNB" src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221012%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221012T183534Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=eb102b2bc9818888486dd17244f5b35443a34e6a7b7faac74496db33c4e5c077" width ="400" height="200"/>

</p>
<h3 align="center">
	<a href="##Description">Description</a>
	<span> · </span>
	<a href="#Compilation-and-testing">Instalation</a>
	<span> · </span>
	<a href="#Compilation-and-testing">Testing</a>
	<span> · </span>
	<a href="#EXEMPLE">EXEMPLE</a>
</h3>

##   <img alt="aitBnB" src="https://cdn.icon-icons.com/icons2/836/PNG/512/Airbnb_icon-icons.com_66791.png" height="30"/> AirBnB clone - The console:

In our Holberton school group project pair programing we work on making a `AirBnB-Console0.1`

## 📖 Description: 
 
<p>
`HolbertonBnB` is a complete web application, integrating database storage, a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.
</p>

###  📦 Storage
All The classes are handled by the  storage engine who it defined in the FileStorage class.
Each time the backend is initialized, HBnB define an instance of FileStorage called storage. 
The storage object loaded and re-loaded from any class instances stored in the JSON file . 

###  💻Console 
The console is a command line interpreter that allow to manage of the backend of HolbertonBnB. It also used to handle and manipulate all classes used by the HBnB.

### 💻Console Commands

 <h3 align="center"> How to Use Command </h3>
---
| Commands | Usage | Description |
| --------- | --------------------------------------------- | ------------------------------------------ |
| `help` | ```help ``` | displays all commands |
| `create` | ```create < class >``` | creates new object |
| `update` | ``` update < class > <id> <attribute> <value>``` | updates attribute of an object |
| `destroy` | ```destroy < class > <id>```| destroys specified object |
| `show` | ``` show < class > <id> ``` | show an object from a file, a database |
| `all` | ``` all < class > ```  |display all objects in class |
| `quit` | ``` quit ``` | exits |
| `EOF` | ```  ``` | exits |
	
##  🛠️ Installation
To use HBnB clone console you need to:

```{r mon_bloc, echo = FALSE, WARNING = TRUE}
git clone .
```
To use the command interpreter hbnb in an interactive mode:
```{r mon_bloc, echo = FALSE, WARNING = TRUE}
./console
``` 

## 🛠️  Compilation and testing

#### 🔧 We are compiling via:
```{r mon_bloc, echo = FALSE, WARNING = TRUE}
```
###  📑Requirement

### 🎥 EXEMPLE/ Usage

## 📂What our file stand for:


<style type="text/css">
.tg  {border-collapse:collapse;border-color:#ccc;border-spacing:0;}
.tg td{background-color:#fff;border-color:#ccc;border-style:solid;border-width:1px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:1px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-oqs5{background-color:#f9f9f9;border-color:#ffffff;text-align:left;vertical-align:top}
.tg .tg-zg5n{border-color:#ffffff;color:#000000;font-size:16px;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-zylj{border-color:#ffffff;color:#000000;font-size:16px;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-vw9p{background-color:#f9f9f9;border-color:#ffffff;font-size:14px;text-align:left;vertical-align:top}
.tg .tg-dvqx{background-color:#f9f9f9;border-color:#ffffff;text-align:center;vertical-align:top}
.tg .tg-2t70{border-color:#ffffff;font-size:14px;text-align:center;vertical-align:top}
.tg .tg-ysfy{border-color:#ffffff;font-size:14px;text-align:left;vertical-align:top}
</style>
<table class="tg" style="undefined;table-layout: fixed; width: 821px">
<colgroup>
<col style="width: 113px">
<col style="width: 152px">
<col style="width: 219px">
<col style="width: 337px">
</colgroup>
<thead>
  <tr>
    <th class="tg-zg5n">diractory</th>
    <th class="tg-zg5n">subdir</th>
    <th class="tg-zylj">file</th>
    <th class="tg-zg5n">discription</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-vw9p" rowspan="18">Hbnb</td>
    <td class="tg-dvqx" colspan="2">console</td>
    <td class="tg-oqs5"></td>
  </tr>
  <tr>
    <td class="tg-2t70" colspan="2">readme</td>
    <td class="tg-ysfy"></td>
  </tr>
  <tr>
    <td class="tg-vw9p" rowspan="7">Models</td>
    <td class="tg-vw9p">base_model</td>
    <td class="tg-vw9p"></td>
  </tr>
  <tr>
    <td class="tg-ysfy">user</td>
    <td class="tg-ysfy"></td>
  </tr>
  <tr>
    <td class="tg-vw9p">amenity</td>
    <td class="tg-vw9p"></td>
  </tr>
  <tr>
    <td class="tg-ysfy">city</td>
    <td class="tg-ysfy"></td>
  </tr>
  <tr>
    <td class="tg-vw9p">place</td>
    <td class="tg-vw9p"></td>
  </tr>
  <tr>
    <td class="tg-ysfy">review</td>
    <td class="tg-ysfy"></td>
  </tr>
  <tr>
    <td class="tg-vw9p">__init__</td>
    <td class="tg-vw9p"></td>
  </tr>
  <tr>
    <td class="tg-ysfy" rowspan="2">Models/engine</td>
    <td class="tg-ysfy">__init__</td>
    <td class="tg-ysfy"></td>
  </tr>
  <tr>
    <td class="tg-vw9p">file_storage</td>
    <td class="tg-vw9p"></td>
  </tr>
  <tr>
    <td class="tg-ysfy" rowspan="6">tests/test_model</td>
    <td class="tg-ysfy">base_model</td>
    <td class="tg-ysfy"></td>
  </tr>
  <tr>
    <td class="tg-vw9p">user</td>
    <td class="tg-vw9p"></td>
  </tr>
  <tr>
    <td class="tg-ysfy">amenity</td>
    <td class="tg-ysfy"></td>
  </tr>
  <tr>
    <td class="tg-vw9p">city</td>
    <td class="tg-vw9p"></td>
  </tr>
  <tr>
    <td class="tg-ysfy">place</td>
    <td class="tg-ysfy"></td>
  </tr>
  <tr>
    <td class="tg-vw9p">review</td>
    <td class="tg-vw9p"></td>
  </tr>
  <tr>
    <td class="tg-ysfy">tests/test_file_storage</td>
    <td class="tg-ysfy">test_file storage</td>
    <td class="tg-ysfy"></td>
  </tr>
</tbody>
</table>
 
## :octocat: Authors:

* [Majdi Aribi](https://github.com/majdideveloper)
* [Hana Ouerghemmi](https://github.com/HanaOuerghemmi)
