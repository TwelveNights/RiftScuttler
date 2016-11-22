import numpy as np
from django.http import HttpResponse
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from playerstatistics.views import playdetail
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def radar_factory(num_vars, frame='circle'):
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)
    theta += np.pi/2

    def draw_poly_patch(self):
        verts = unit_poly_verts(theta)
        return plt.Polygon(verts, closed=True, edgecolor='k')

    def draw_circle_patch(self):
        return plt.Circle((0.5, 0.5), 0.5)

    patch_dict = {'polygon': draw_poly_patch, 'circle': draw_circle_patch}
    if frame not in patch_dict:
        raise ValueError('unknown value for `frame`: %s' % frame)

    class RadarAxes(PolarAxes):

        name = 'radar'
        RESOLUTION = 1
        draw_patch = patch_dict[frame]

        def fill(self, *args, **kwargs):
            closed = kwargs.pop('closed', True)
            return super(RadarAxes, self).fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            lines = super(RadarAxes, self).plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            return self.draw_patch()

        def _gen_axes_spines(self):
            if frame == 'circle':
                return PolarAxes._gen_axes_spines(self)

            spine_type = 'circle'
            verts = unit_poly_verts(theta)

            verts.append(verts[0])
            path = Path(verts)

            spine = Spine(self, spine_type, path)
            spine.set_transform(self.transAxes)
            return {'polar': spine}

    register_projection(RadarAxes)
    return theta


def unit_poly_verts(theta):

    x0, y0, r = [0.5] * 3
    verts = [(r*np.cos(t) + x0, r*np.sin(t) + y0) for t in theta]
    return verts


def fetch_data(pname):
    fetched_data = playdetail(pname)
    data = [
        ['Kill', 'Death', 'Assists', 'WardsPlaced', 'Gold (k)', 'WardsDestroyed', 'CreepCore (10s)',
         '        teamJungle (10s)', '            EnemyJungle (10s)', 'Damage (k)'],
        ('PlayerStatistics', [
            [fetched_data['averageK'], fetched_data['averageD'], fetched_data['averageA'], fetched_data['avgw'],
             (fetched_data['avgg']/1000), fetched_data['avgwd'], fetched_data['avgcs']/10, fetched_data['avgtJungle'], (fetched_data['avgeJungle']/10),
             (fetched_data['avgdmg']/1000)],
            [fetched_data['maxK'], fetched_data['maxD'], fetched_data['maxA'], 0, 0, 0, 0, 0, 0, 0]])
    ]
    return data


def request_radar_plot(request, pname):
    N = 10
    theta = radar_factory(N, frame='polygon')

    data = fetch_data(pname)
    spoke_labels = data.pop(0)

    fig = plt.figure(figsize=(14, 14))

    colors = ['b', 'r']
    for n, (title, case_data) in enumerate(data):
        ax = fig.add_subplot(1, 1, 1, projection='radar')
        plt.rgrids([10, 20, 30, 40])
        ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.1),
                     horizontalalignment='center', verticalalignment='center')
        for d, color in zip(case_data, colors):
            d = np.array(d)
            ax.plot(theta, d, color=color)
            ax.fill(theta, d, facecolor=color, alpha=0.25)
        ax.set_varlabels(spoke_labels)

    plt.subplot(1, 1, 1)
    labels = ('Statistics', 'MaxKDA')
    legend = plt.legend(labels, loc=(0.90, .95), labelspacing=0.2)
    plt.setp(legend.get_texts(), fontsize='small')
    fig.set_facecolor('white')
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
