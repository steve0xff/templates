#!/usr/bin/env python

import logging
TC_PARMs = get_testrail_parms()


class GUI_login-auth():
    init(self):
        prod_version = self.product_version()
        if prod_version < (1, 0):
            self.fail('Versions < 1.0 are no longer supported')

    @attr(phase='smoke')
    def c1(self):
        """Doc String here"""
        site_url = TC_PARMS.pop(1)
        login = TC_PARAMS.pop(2)
        pass = TC_PARAMS.pop(3)

        self.assertTrue(TryLogin(Site_url, login, pass))
    
    @attr(phase='smoke')
    def c2(self):
        """Doc String here"""
        site_url = TC_PARMS.pop(1)
        login = TC_PARAMS.pop(2)
        pass = TC_PARAMS.pop(3)

        self.assertTrue(PositiveLoginAttempt(Site_url, login, pass))
