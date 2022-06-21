repo_name=$1
repo_dir=$(echo ${repo_name} | cut -d '/' -f 2)
cd /home/runner/work/${repo_dir}/${repo_dir}
rm docker-compose.yml
wget https://raw.githubusercontent.com/NebraLtd/helium-miner-software/master/device-compose-files/docker-compose-rpi.yml -O docker-compose.yml