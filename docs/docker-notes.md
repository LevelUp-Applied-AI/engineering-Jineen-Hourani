# Docker Notes — Day 9

## Docker Version

Command used:

```
docker version
```

Output:

```
Client:
 Version:           29.2.1
 API version:       1.53
 Go version:        go1.25.6
 Git commit:        a5c7197
 Built:             Mon Feb  2 17:20:16 2026
 OS/Arch:           windows/amd64
 Context:           desktop-linux

Server: Docker Desktop 4.63.0 (220185)
 Engine:
  Version:          29.2.1
  API version:      1.53 (minimum version 1.44)
  Go version:       go1.25.6
  Git commit:       6bc6209
  Built:            Mon Feb  2 17:17:24 2026
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          v2.2.1
 runc:
  Version:          1.3.4
 docker-init:
  Version:          0.19.0
```

Docker Desktop is running with the WSL2 backend and the Docker Engine is active.

---

# Docker Info

Command used:

```
docker info
```

Important parts of the output:

```
Server Version: 29.2.1
Storage Driver: overlayfs
Kernel Version: 6.6.87.2-microsoft-standard-WSL2
Operating System: Docker Desktop
Architecture: x86_64
CPUs: 8
Total Memory: 3.824GiB
Docker Root Dir: /var/lib/docker
```

This confirms that Docker is running correctly using the WSL2 backend.

---

# Hello World Test

Command used:

```
docker run hello-world
```

Output:

```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from Docker Hub.
 3. The Docker daemon created a new container from that image.
 4. The container executed the hello-world program and returned the output.
```

This confirms that Docker can successfully pull images and run containers.

---

# Docker Images

Command used:

```
docker images
```

Output:

```
IMAGE                             ID             DISK USAGE   CONTENT SIZE
docker/welcome-to-docker:latest   c4d56c24da4f       22.2MB         6.03MB
hello-world:latest                ef54e839ef54       25.9kB         9.52kB
postgres:15-alpine                fceb6f86328c        392MB          110MB
```

This confirms that the postgres:15-alpine image was successfully pulled and stored locally.

---

# Running the Postgres Container

Command used:

```
docker run -d \
  --name pg-prework \
  -e POSTGRES_PASSWORD=prework \
  -p 5432:5432 \
  postgres:15-alpine
```

Verify container is running:

```
docker ps
```

Output:

```
CONTAINER ID   IMAGE                COMMAND                  CREATED       STATUS          PORTS                                       NAMES
f0991253dd50   postgres:15-alpine   "docker-entrypoint.s…"   4 hours ago   Up 30 seconds   0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp  pg-prework
```

This confirms that the Postgres container is running and the database port is exposed.

---

# Startup Logs

Command used:

```
docker logs pg-prework
```

Relevant startup logs:

```
waiting for server to start....
LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl
LOG:  listening on IPv4 address "0.0.0.0", port 5432
LOG:  listening on IPv6 address "::", port 5432
LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
LOG:  database system was shut down
LOG:  database system is ready to accept connections
```

Startup confirmation line:

```
LOG: database system is ready to accept connections
```

This confirms the PostgreSQL database server started successfully inside the container.

---

# Stop and Restart

Stop command used:

```
docker stop pg-prework
```

Output:

```
pg-prework
```

Verify no running containers:

```
docker ps
```

Output:

```
CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS   PORTS   NAMES
```

Check stopped containers:

```
docker ps -a
```

Output:

```
CONTAINER ID   IMAGE                             STATUS
f0991253dd50   postgres:15-alpine                Exited (0)
c6ed5e56b463   hello-world                       Exited (0)
1ea0cbfd3004   docker/welcome-to-docker:latest   Exited (0)
```

Restart command:

```
docker restart pg-prework
```

Output:

```
pg-prework
```

Verify running again:

```
docker ps
```

Output:

```
CONTAINER ID   IMAGE                COMMAND                  STATUS         PORTS                     NAMES
f0991253dd50   postgres:15-alpine   "docker-entrypoint.s…"   Up 30 seconds  0.0.0.0:5432->5432/tcp    pg-prework
```

Logs after restart:

```
docker logs pg-prework
```

Relevant line confirming successful startup:

```
LOG: database system is ready to accept connections
```

This confirms the container restarted successfully.

---

# Issues Encountered

Docker Desktop initially failed to start after allocating 4GB of memory in the `.wslconfig` configuration file.

The issue was resolved by reducing system RAM usage, closing background applications, and restarting the machine. After rebooting, Docker Desktop started normally and all Docker validation steps worked successfully.
