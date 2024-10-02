from odoo import http
from odoo.http import request

class AuthController(http.Controller):
    
    @http.route('/custom/login', type='http', auth='public', website=True)
    def custom_login(self, **kw):
        return request.render('grafana_login.login_template', {})

    @http.route('/custom/register', type='http', auth='public', website=True)
    def custom_register(self, **kw):
        return request.render('grafana_login.register_template', {})

    @http.route('/custom/login/submit', type='http', auth='public', methods=['POST'], website=True, csrf=False)
    def login_submit(self, **kw):
        login = kw.get('login')
        password = kw.get('password')

        try:
            request.session.authenticate(request.db, login, password)
            return request.redirect('/custom/dashboard')
        except Exception as e:
            return request.redirect('/custom/login?error=1')

    @http.route('/custom/register/submit', type='http', auth='public', methods=['POST'], website=True, csrf=False)
    def register_submit(self, **kw):
        user = request.env['res.users'].sudo().create({
            'name': kw.get('name'),
            'login': kw.get('login'),
            'password': kw.get('password'),
            'phone': kw.get('phone'),
            'address': kw.get('address'),
        })
        request.env.cr.commit()
        return request.redirect('/custom/login')

    
    @http.route('/custom/dashboard', type='http', auth='user', website=True)
    def dashboard(self, **kw):
        return request.render('grafana_login.dashboard_template', {})
    
    @http.route('/custom/logout', type='http', auth='user', website=True)
    def logout(self):
        request.session.logout()
        return request.redirect('/custom/login')
