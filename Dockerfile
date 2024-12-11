FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y wget && \
    wget -O /usr/local/bin/cloudflared https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 && \
    chmod +x /usr/local/bin/cloudflared

EXPOSE 7860

RUN --mount=type=secret,id=TUNNEL_TOKEN,mode=0444,required=true
CMD ["bash", "-c", "python -m bot & cloudflared tunnel --url http://localhost:7860 --token $(cat /run/secrets/TUNNEL_TOKEN)]