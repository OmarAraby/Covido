<h1>Covido Django Project ( Graduation Project )</h1>

 
<h2 align="left"> Quick Note  </h2>
<p> The Frontend Template from this <a href="https://github.com/kaushikjadhav01">Repo</a>

Covido Django Project a web application Built Using Django Framework and and (html - css - js) Templates that helping people to get information of the confirmed, recovery and deaths cases. 
Covido can forecast the near future, trying to help people to reduce the feeling of danger because it makes the virus statistically and aware of its dimensions.
</p>


<h2 align="left"> Features </h2>

* The main idea is to track Corona virus cases (Susceptible, Exposed, Infectious, and Removed or Recovered) By collecting data from more than one reliable source, then generate a forecasting models to for cast the near future death, recovery and new cases.

* if a user needs to know if he is effected or not he can put his chest X-Ray Covido will predict, any user can tracing hospitals eligible to receive cases also follow where there are places for the injured or not, and where they are, also Doctors can give their advice in posts, users can reply to theirs.

* Update ---> Two Years ago the daily data for death, recovery and new cases are available and there are many APIs provided them , Right now the Data sources are scarce , so currently I rely on available data, and the data are not daily collection 

<h2 align="left"> Team Members </h2>

* Omar Mahamad Araby --> (Django backend - API - Data Visualization)
* Karim Al-Amir Ahmad --> (Django backend - API)
* Abdelrahman Ruby --> ( Chest X-Ray Model )
* Mariam Sabry Muhammad --> ( Death , Recovery and New Cases Forecasting Model)


<h2 align="left"> Getting Started </h2>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

<h4>Prerequisites <br></h4>
You will need to have the following software installed on your system:

* Python (3.7 or later)


<h2 align="left"> Installation:</h2>
<h4>Step 1: clone the repo <br></h4>
<h4>Step 2: Make Sure to  install python and pip<br></h4>

<h4>Step 3: create your virtual environment <br></h4>


```python
python -m venv NAME_of_Your_Environment
NAME_of_Your_Environment\Srctipt\Activate
```


<h4>Step 4: install required liberies <br> </h4>

```python
pip install -r requirements.txt
```


<h4>  Step 5: Run migrations and create a db. from cmd type </h4>

```python
python manage.py makemigrations
python manage.py migrate
```
* If You want to clear Database
```python
python manage.py migrate --run-syncdb
```

<h4> Step 6: create a superuser to get an access the admin panal</h4>

```python
python manage.py createsuperuser
```

<h4> Step 7: Run Server </h4>

```python
python manage.py runserver
```


<h2 align="left"> ScreenShots</h2>

Admin Panal

![image](https://github.com/OmarAraby/Covido/assets/55214550/55b9752c-db74-404a-af59-a803152e3a16)




![image](https://github.com/OmarAraby/Covido/assets/55214550/832ec26a-31c9-4ee5-9531-432fd5eea8e2)


![image](https://github.com/OmarAraby/Covido/assets/55214550/691c66f2-abc3-4fd4-bdcc-9490dec5ce4e)

![image](https://github.com/OmarAraby/Covido/assets/55214550/e3193c51-9b6b-416f-8437-c7351ab50c06)

![image](https://github.com/OmarAraby/Covido/assets/55214550/fa09954c-586f-4fae-bc79-e399e76c2618)

![image](https://github.com/OmarAraby/Covido/assets/55214550/96f430c8-89f0-4187-bc9d-f6f8e9bd009b)

![image](https://github.com/OmarAraby/Covido/assets/55214550/f50d4d49-0eed-40c7-91cc-19c3915f281f)

![image](https://github.com/OmarAraby/Covido/assets/55214550/5f6ae15b-e1dd-454c-ad07-4b448a5250d3)









