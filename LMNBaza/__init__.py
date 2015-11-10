# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LMNBaza
                                 A QGIS plugin
 Import danych do aplikacji mapowych
                             -------------------
        begin                : 2015-11-05
        copyright            : (C) 2015 by Krzysztof Kin
        email                : krzysztof.kin@szczecinek.lasy.gov.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LMNBaza class from file LMNBaza.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .lmnbaza import LMNBaza
    return LMNBaza(iface)
