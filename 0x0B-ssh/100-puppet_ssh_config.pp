# Ensure the SSH config file exists
file { '/home/ubuntu/alx-system_engineering-devops/0x0B-ssh/100-puppet_ssh_config.pp':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
}

# Declare the IdentityFile line to use the private key ~/.ssh/school
file_line { 'Declare identity file':
  path  => '/home/ubuntu/alx-system_engineering-devops/0x0B-ssh/100-puppet_ssh_config.pp',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile',
}

# Turn off password authentication
file_line { 'Turn off passwd auth':
  path  => '/home/ubuntu/alx-system_engineering-devops/0x0B-ssh/100-puppet_ssh_config.pp',
  line  => 'PasswordAuthentication no',
  match => '^PasswordAuthentication',
}
IdentityFile ~/.ssh/school
PasswordAuthentication no
