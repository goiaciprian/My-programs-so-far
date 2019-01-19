
"""
Nu mai stiu ce voiam sa fac aici...
"""

from plotly.offline import init_notebook_mode, iplot
from IPython.display import display, HTML

import numpy as np

init_notebook_mode(connected=True)

N = 50
s = np.linspace(-1, 1, N)
vx = 1 + 2 * s
vy = 1 - 2 * s  # v=(vx, vy) is the velocity
speed = np.sqrt(vx ** 2 + vy ** 2)
ux = vx / speed  # (ux, uy) unit tangent vector, (-uy, ux) unit normal vector
uy = vy / speed

xend = xx + ux  # end coordinates for the unit tangent vector at (xx, yy)
yend = yy + uy

xnoe = xx - uy  # end coordinates for the unit normal vector at (xx,yy)
ynoe = yy + ux

data = [dict(x=x, y=y,
             name='frame',
             mode='lines',
             line=dict(width=2, color='blue')),
        dict(x=x, y=y,
             name='curve',
             mode='lines',
             line=dict(width=2, color='blue'))
        ]

layout = dict(width=600, height=600,
              xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
              yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
              title='Moving Frenet Frame Along a Planar Curve', hovermode='closest',
              updatemenus=[{'type': 'buttons',
                            'buttons': [{'label': 'Play',
                                         'method': 'animate',
                                         'args': [None]}]}])

frames = [dict(data=[dict(x=[xx[k], xend[k], None, xx[k], xnoe[k]],
                          y=[yy[k], yend[k], None, yy[k], ynoe[k]],
                          mode='lines',
                          line=dict(color='red', width=2))
                     ]) for k in range(N)]

figure2 = dict(data=data, layout=layout, frames=frames)
iplot(figure2)
