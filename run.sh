# Build ./ with the name devoo and version latest
docker build -t devoo:latest .
docker run -d --restart unless-stopped devoo:latest