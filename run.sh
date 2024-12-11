python -m bot &
cloudflared tunnel --url http://localhost:7860 --token $(cat /run/secrets/TUNNEL_TOKEN)