import json

import pandas as pd
from django.db import connection
from django.http import HttpResponse
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Gauge
from pyecharts.charts import Line
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType
from rest_framework.views import APIView


# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


def exc_sql(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def day_user():
    # query_sql = "SELECT DATE_FORMAT(date_joined, '%Y-%m-%d')as time, COUNT(*) as COUNT" \
    #             " from users group by time "
    # data_list = exc_sql(query_sql)
    date_joined_list = [1,2,3,4,5,6,7]
    count_list = [10,20,23,14,6,11,3]

    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
            .add_xaxis(xaxis_data=date_joined_list)
            .add_yaxis(
            series_name="",
            y_axis=count_list,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
            areastyle_opts=opts.AreaStyleOpts(opacity=1, color="#C67570"),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Weekly User Number", pos_left="center"),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        )
            .dump_options_with_quotes()
    )
    return c


class Day_userView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(day_user()))


def day_order():
    # query_sql = "SELECT DATE_FORMAT(order_time, '%Y-%m-%d')as time, COUNT(*) as COUNT" \
    #             " from orders group by time "
    # data_list = exc_sql(query_sql)
    # print(data_list)
    order_time_list = [1,2,3,4,5,6,7]
    count_list = [12,3,24,21,3,21,4]
    c = (
        Bar()
            .add_xaxis(order_time_list)
            .add_yaxis('Weekly Order Number', count_list, color="#84CCC9")
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            datazoom_opts=opts.DataZoomOpts(),

        )
            .dump_options_with_quotes()
    )
    return c


class Day_orderView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(day_order()))


def season_order():
    # query_sql = "SELECT DATE_FORMAT(order_time, '%Y-%m-%d')as time, COUNT(*) as COUNT" \
    #             " from orders group by time "

    #data_list = exc_sql(query_sql)
    order_time_list = [1,2,3,4]
    count_list = [10,22,30,15]
    data = {'Date': order_time_list,
            'count': count_list}
    df = pd.DataFrame(data)

    df.set_index("Date", inplace=True)
    df.index = pd.to_datetime(df.index)
    df = df.resample('Q').sum()
    count = df['count'].values.tolist()
    x = ["first", "second ", "third", "forth"]
    data_pair = [list(z) for z in zip(x, count)]
    c = (
        Pie(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add(
            series_name="order number",
            data_pair=data_pair,
            rosetype="radius",
            radius="55%",
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Seasonal Order number",
                pos_left="center",
                pos_top="20",
                title_textstyle_opts=opts.TextStyleOpts(color="#000"),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
            .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            label_opts=opts.LabelOpts(color="rgba(0, 0, 0, 0.5)"),
        )
            .dump_options_with_quotes()
    )
    return c


class Season_orderView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(season_order()))


def user_number():
    query_sql = "SELECT COUNT(*) as COUNT from users"
    count_list = exc_sql(query_sql)
    # print(count_list)
    c = (
        Gauge(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add(
            "",
            [("Total", count_list)],
            split_number=5,
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
                )
            ),
            detail_label_opts=opts.LabelOpts(formatter="{value}"),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Total User Number", pos_left="center"),
            legend_opts=opts.LegendOpts(is_show=False),

        )
            .dump_options_with_quotes()

    )
    return c


class User_numberView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(user_number()))


def goods_number():
    query_sql = "SELECT COUNT(*) as COUNT from goods"
    count_list = exc_sql(query_sql)
    c = (
        Gauge(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add(
            "",
            [("Total", count_list)],
            split_number=5,
            detail_label_opts=opts.LabelOpts(formatter="{value}"),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
                )
            ))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Total Good Number", pos_left="center"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
            .dump_options_with_quotes()

    )
    return c


class Goods_numberView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(goods_number()))


def order_number():
    query_sql = "SELECT COUNT(*) as COUNT from orders"
    count_list = exc_sql(query_sql)
    c = (
        Gauge(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add(
            "",
            [("Total", count_list)],
            split_number=5,
            detail_label_opts=opts.LabelOpts(formatter="{value}"),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
                )
            )
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Total Order Number", pos_left="center"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
            .dump_options_with_quotes()

    )
    return c


class Order_numberView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(order_number()))


def season_user():
    # query_sql = "SELECT DATE_FORMAT(date_joined, '%Y-%m-%d')as time, COUNT(*) as COUNT" \
    #             " from users group by time "
    #
    # data_list = exc_sql(query_sql)
    user_time_list = [1,2,3,4]
    count_list = [20,31,19,6]
    data = {'Date': user_time_list,
            'count': count_list}
    df = pd.DataFrame(data)

    df.set_index("Date", inplace=True)
    df.index = pd.to_datetime(df.index)
    df = df.resample('Q').sum()
    count = df['count'].values.tolist()
    x = ["first", "second ", "third", "forth"]
    data_pair = [list(z) for z in zip(x, count)]
    c = (
        Pie(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add(
            series_name="user number",
            data_pair=data_pair,
            rosetype="radius",
            radius="55%",
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Seasonal User number",
                pos_left="center",
                pos_top="20",
                title_textstyle_opts=opts.TextStyleOpts(color="#000"),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
            .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            label_opts=opts.LabelOpts(color="rgba(0, 0, 0, 0.5)"),
        )
            .dump_options_with_quotes()
    )
    return c


class Season_userView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(season_user()))
