from app.public_views import *
from app.methods.alphabet_dict_maker import AlphabetDictMaker


@app.route('/country')
def country():
    img = GetPhoto(search_object='coffee shop')
    image = img.final
    try:
        page = int(request.args.get('index'))
    except TypeError:
        page = 1
    dict_maker = AlphabetDictMaker()
    dict_maker.ret_alphabetical_country()
    alphabet_country_list = dict_maker.ret_item_by_index(index=page)
    return render_template('public/country.html',
                           user=current_user,
                           countrys=alphabet_country_list,
                           alphabet=dict_maker.upper_alphabet,
                           title="Country List",
                           image=image,
                           alpha_lower=dict_maker.upper_alphabet,
                           page=page, )


