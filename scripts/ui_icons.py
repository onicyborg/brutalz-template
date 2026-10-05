"""Small directional icons shared by standalone page builders."""
def arrow(direction='right'):
    paths = {'left': 'M20 12H4m6-6-6 6 6 6', 'right': 'M4 12h16m-6-6 6 6-6 6',
             'chevron-left': 'm15 18-6-6 6-6', 'chevron-right': 'm9 18 6-6-6-6'}
    return f'<svg class="icon icon-arrow-sm" aria-hidden="true" viewBox="0 0 24 24"><path d="{paths[direction]}"/></svg>'
