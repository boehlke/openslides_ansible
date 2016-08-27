# You may want this to run as user root instead
# or make this an environmental variable, or
# a CLI prompt. Whatever you want!

import task

become_user_password = 'foo-whatever'
run_data = {
    'user_id': 12345,
    'foo': 'bar',
    'baz': 'cux-or-whatever-this-one-is'
}

runner = task.Runner(
    hostnames='172.17.0.7',
    playbook='../play/os_play.yaml',
    private_key_file='/home/user/.ssh/id_rsa.pub',
    run_data=run_data,
    become_pass=become_user_password,
    verbosity=0
)

stats = runner.run()

# Maybe do something with stats here? If you want!

print stats
