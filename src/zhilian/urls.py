from src.zhilian import zhilian_app
from .views import JobItemView, CompanyItemView, RelationItemView

zhilian_app.add_url_rule("/jobs", view_func=JobItemView.as_view('jobs'), methods=["GET"])
zhilian_app.add_url_rule("/company", view_func=CompanyItemView.as_view('company'), methods=["GET"])
zhilian_app.add_url_rule("/relation", view_func=RelationItemView.as_view('relation'), methods=["GET"])
