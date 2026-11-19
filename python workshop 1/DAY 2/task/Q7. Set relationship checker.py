required = {'loops', 'functions'}
completed = {'variables', 'loops', 'functions', 'lists'}
if len(completed-required) == abs(len(completed)-len(required)) :
    print(True)
else:
    print(False)