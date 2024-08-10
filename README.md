# FlaskApp
git remote -v
git config --global user.email "prem4eru@gmail.com"
git config --global user.name "prem4eru"git remote -v
git push origin main
python .\app.py
docker build -t flask-app .
docker build -t flask-app .
docker images
docker run -d - p 5000:5000 flask-app
docker run -d -p 5000:5000 flask-app
docker tag flask-app prem4eru/flask-app
docker login
docker push prem4eru/flask-app
git add .
git commit -m "completed docker flask app"
git push origin main