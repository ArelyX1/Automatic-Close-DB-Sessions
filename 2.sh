#!/bin/bash

while true; do
  .venv/bin/python3 2.py

  archivo="LOG/pids.txt"

  while read pid; do
    if kill -0 "$pid" 2>/dev/null; then
      echo "Eliminando PID $pid"
      sudo kill -9 "$pid"
    else
      echo "PID $pid no existe o ya fue terminado."
    fi
  done < "$archivo"
  rm "$archivo"
  awk '/Mem:/ {printf("Free memory: %d%%\n", int($7/$2 * 100))}' <(free -m)
  .venv/bin/python3 sql.py "$(awk '/Mem:/ {printf("%d", int($7/$2 * 100))}' <(free -m))" 02

  sleep 60
done  
