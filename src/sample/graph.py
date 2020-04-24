import pyecharts
from pyecharts.charts import Bar
from pyecharts import options
from pyecharts.globals import ThemeType
from pyecharts.charts import Gauge, Page, Grid
from pyecharts.components import Table
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot
from pyecharts.options import ComponentTitleOpts

def version():
    print(pyecharts.__version__)


def draw_bar() -> Bar:
    """
    柱状图
    :return:
    """
    bar = Bar(init_opts=options.InitOpts(theme=ThemeType.DARK))
    bar.add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月"])
    bar.add_yaxis("商家A", [5, 12, 166, 12, 23, 34])
    bar.add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    # 标题
    bar.set_global_opts(title_opts=options.TitleOpts(title="主标题", subtitle="副标题"))
    return bar


def draw_gauge() -> Gauge:
    c = Gauge(init_opts=options.InitOpts(theme=ThemeType.DARK))
    c.add("", [("完成率", 66.6)])
    c.set_global_opts(title_opts=options.TitleOpts(title="基本用法"))
    return c


def draw_table() -> Table:
    table = Table()
    headers = ["City name", "Area", "Population", "Annual Rainfall"]
    rows = [
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Adelaide", 1295, 1158259, 600.5],
    ]
    table.add(headers, rows)
    return table



if __name__ == '__main__':
    page = Page()
    page.add(draw_bar())
    page.add(draw_gauge())
    page.add(draw_table())
    # 生成 html 文件
    page.render()

    # 生成 图片 ，需要安装 phantomjs，并配置 path
    # make_snapshot(snapshot, draw_table().render(), 'bar0.png')


