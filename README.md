# ml-endpoint-docker-gunicorn README

- Create docker image with `Flask` [<img src= "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/120px-Flask_logo.svg.png" alt="Flasklogo" height="5%" width="5%" title="Flask">](https://github.com/pallets/flask) and `Gunicorn`[<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Gunicorn_logo_2010.svg/120px-Gunicorn_logo_2010.svg.png" alt="Gunicorn" height="5%" width="5%" title="Flask">](https://github.com/benoitc/gunicorn) web framework to act as a API server. ML details is [available at](https://github.com/tamjid-ahsan/capstone_customer_churn).


# Instruction

- build image from Docker file

    ``` bash
    docker build -t ml-model-churn .
    ```

- run server

    ``` bash
    docker run -d -p 5000:5000 ml-model-churn
    ```

    <b>OR</b>

    ```
    docker run --name ml -d -p 5000:5000 ml-model-churn
    ```

    - previously run container

    ```bash
    docker start <CONTAINER> # ml
    ```
### usefull commands

- list all running

    ``` bash
    docker ps
    ```

- docker build cache cleanup

    ```bash
    docker builder prune
    ```

- reference:

    1. [docker-using-flask](https://medium.com/swlh/machine-learning-model-deployment-in-docker-using-flask-d77f6cb551d6)
    2. [install-python3-on-amazon-linux-2](https://devopsmania.com/how-to-install-python3-on-amazon-linux-2/)
    3. [ai-rest-api](https://medium.com/dataswati-garage/create-a-robust-ai-rest-api-71a8050ce314)

___
contact: <a href="mailto:tamz888@yahoo.com">tamz888@yahoo.com</a> [<img src="data\TAlogo1.png" alt="TA" height="3%" width="3%">](http://linkedin.com/in/tamjidahsan/)
___

# TODO:

- reduce deployment size
    - base image
    - modify packages and libraries
- fix README
- deploy to cloud to use in front-end WebApp built on JavaScript or TypeScript

___
**test this server** using this curl command after using docker for deployment.

```bash
# gunicorn server
curl --location --request POST 'http://localhost:5000/predict' --header 'Content-Type: application/json' --data-raw '{"Customer_Age": 45, "Gender": "M", "Dependent_count": 3, "Education_Level": "High School", "Marital_Status": "Married", "Income_Category": "60K_to_80K", "Card_Category": "Blue", "Months_on_book": 39, "Total_Relationship_Count": 5, "Months_Inactive_12_mon": 1, "Contacts_Count_12_mon": 3, "Credit_Limit": 12691.0, "Total_Revolving_Bal": 777, "Avg_Open_To_Buy": 11914.0, "Total_Amt_Chng_Q4_Q1": 1.335, "Total_Trans_Amt": 1144, "Total_Trans_Ct": 42, "Total_Ct_Chng_Q4_Q1": 1.625, "Avg_Utilization_Ratio": 0.061}'
```