# MCP with Ollama
A chatbot that uses the MCP protocol to talk to network devices.  

1. Start MCP server 2. Run python client

**Activate the environment**  
```
source myenv/bin/activate  # Linux/Mac
```

**Inspiration**: [Building Your First Agentic AI: Complete Guide to MCP + Ollama Tool Calling](https://dev.to/ajitkumar/building-your-first-agentic-ai-complete-guide-to-mcp-ollama-tool-calling-2o8g)  
## FFRouting

It is a "software that implements and manages various IPv4 and IPv6 routing protocols."
Docker image: [ frrouting / frr](https://quay.io/repository/frrouting/frr)

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

Python can be used to run container.exec_run("vtysh -c 'show running-config'")
