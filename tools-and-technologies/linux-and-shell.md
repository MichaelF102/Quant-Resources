# Linux and shell

*Last reviewed: Oct 2026*

Most of the work in this program happens in a terminal on Linux, or on Windows through WSL. This page covers the shell skills you use every day, the tools that save time, and the system settings that matter for data pipelines and benchmarks.

## 1. Shell basics

You need these without looking them up:

- Moving and listing: `cd`, `ls -lh`, `pwd`, `tree`.
- Reading files: `less`, `head`, `tail -f`, `wc -l`.
- Searching: `grep`, `find`, and the faster `rg` (below).
- Processing text: pipes, `cut`, `sort`, `uniq -c`, `awk` for simple column work.
- Permissions and processes: `chmod`, `ps aux`, `kill`, `top` or `htop`.
- Redirection and loops: `>`, `>>`, `2>&1`, and `for f in *.csv; do ...; done`.

Use the shell to check data before loading it. For example, `wc -l` on a bhavcopy archive tells you whether a day's file is complete.

## 2. Search and navigation

| Tool | Use it for | Verdict | Link |
|---|---|---|---|
| ripgrep (`rg`) | Searching code and data quickly, respecting `.gitignore` | Faster and simpler than `grep -r` for code. | [Repository](https://github.com/BurntSushi/ripgrep) |
| `fd` | Finding files by name | Simpler than `find` for common cases. | — |
| `fzf` | Interactive filtering of history and files | Useful once you have many files. | — |

## 3. Terminal multiplexing

| Tool | Use it for | Verdict | Link |
|---|---|---|---|
| tmux | Keeping sessions alive across disconnects, with several panes | Essential for long runs on a remote machine. Learn `new -s`, `attach`, `detach` and split panes. | [Repository](https://github.com/tmux/tmux) |
| `screen` | The older alternative to tmux | Use tmux instead. |

## 4. Remote work

- `ssh` with key-based login. Never share a password in a script.
- `scp` or `rsync` to move files. `rsync` is the better choice for large directories, because it resumes and copies only changes.
- Use `~/.ssh/config` for host aliases, so the command is short.

## 5. Scheduling daily jobs

A data pipeline that runs every evening needs a scheduler. Two options:

- **cron** is simple and everywhere. Add a line with `crontab -e`. Use absolute paths, set `PATH` at the top of the crontab, and redirect output to a log file.
- **systemd timers** are the modern option on Linux. They log to the journal, can catch up after a missed run, and fit the service-based design of a production system.

For either, the job must be **idempotent**: running it twice must produce the same output. See [Databases and storage](databases-and-storage.md).

## 6. Time zones

Exchange data is in IST (UTC+05:30). Set the zone explicitly rather than trusting the machine:

```
TZ=Asia/Kolkata
```

Store timestamps in UTC inside your pipeline, and convert for display. A job that runs at 18:00 local time on a server in another zone produces a different date.

## 7. Benchmarks and CPU settings

- Pin a benchmark to a core with `taskset -c 2 ./bench`, so it doesn't move between cores during the run.
- Check the CPU governor (`cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor`). A `powersave` governor changes timings. Record the setting with your results.
- Close other programs, and run the benchmark several times.

These steps reduce noise. They do not make a result comparable across machines. Record the hardware in every benchmark README.

## 8. WSL

On Windows, WSL2 gives a full Linux environment. It is enough for every project in this repo, but:

- Keep project files inside the Linux file system (`~/projects`), not under `/mnt/c`. File I/O is much slower across the boundary.
- Hardware counters for `perf` are often unavailable in WSL. Profile on a native Linux machine when you need them.

## 9. Learn when

| Phase | Learn |
|---|---|
| QR Phase 0 | Shell basics, `rg`, tmux, `ssh` |
| QR Phase 3 | Scheduling and idempotent jobs, when you automate a data update |
| QD Phase 0 | All of the above, plus `taskset` and CPU governors |
| QD Phase 3 | `strace`, process and thread inspection |
| QD research track | cron or systemd timers for the data pipeline checkpoint |
