def main(params):
    step = params['step'] if 'step' in params else 0

    if step == 0:
        return {
            'action': 'absoluteProduct/multiply',
            'params': params,
            'state': { 'step': step + 1 }
        }

    if step == 1:
        return {
            'action': 'absoluteProduct/absolute',
            'params': params,
            'state': { 'step': step + 1 }
        }
    
    if step == 2:
        del params['step']
        return params
