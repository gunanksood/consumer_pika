docker pull gunanksood/producer_image
docker pull gunanksood/consumer_image
docker run -p 5000:5000 -d gunanksood/producer_image
docker run -p 5001:5001 -d gunanksood/consumer_image
docker-compose up -d
docker logs -f <Container ID of consumer>
Now open the browser and type 127.0.0.1:5000
upload the csv file present in the zip Extracted folder.



