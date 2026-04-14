# MCP with Ollama
A chatbot that uses the MCP protocol to talk to network devices.   

TASK: don't think I need all those requiremetsn but only the ones in the server.  

## Architecture Diagram
![architecure_diagram](./docs/images/architecure_diagram.png)

## Open WebUI Container
```
docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always openwebui/open-webui
```
Source: [Installation with Default Configuration](https://github.com/open-webui/open-webui#troubleshooting)
Put this in mcp connector: http://localhost:9090/mcp
and activate the tool in the chat interface

## FRRouting Container
```
sudo docker run -d --privileged --name my-frr --net=host frrouting/frr:v8.4.0
```

## FastMCP Server Containter

**Activate the environment**  
```
source myenv/bin/activate  # Linux/Mac
python mcp-server/server.py
```

**Inspiration**: [Building Your First Agentic AI: Complete Guide to MCP + Ollama Tool Calling](https://dev.to/ajitkumar/building-your-first-agentic-ai-complete-guide-to-mcp-ollama-tool-calling-2o8g)  
## FFRouting

It is a "software that implements and manages various IPv4 and IPv6 routing protocols."
Docker image: [ frrouting / frr](https://hub.docker.com/r/frrouting/frr)

Initial workflow  
```
root@hp-laptop:~$ docker run -d --privileged --name my-frr --net=host frrouting/frr:v8.4.0  # pulls img and starts it if not present
root@hp-laptop:~$ docker exec -it my-frr /bin/bash  # enters container env
bash-5.1# vtysh
hp-laptop# show running-config 
Building configuration...

Current configuration:
!
frr version 8.4_git
frr defaults traditional
hostname hp-laptop
no ipv6 forwarding
!
end
hp-laptop#  
bash-5.1# 
exit
```

Stopping the container
```
docker stop my-frr
```
