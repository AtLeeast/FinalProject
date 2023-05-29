from ..models import AccountModel


def get_user_data(request):
    authorized = "account_id" in request.session
    data = {
        "authorized": authorized,
    }

    if authorized:
        account_id = request.session["account_id"]
        account = AccountModel.objects.filter(id=account_id)[0]
        data["email"] = account.email
        data["bottles"] = account.bottles
        data["bottles_today"] = account.bottles_today

    return data
