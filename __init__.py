# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SystemSelectCoordinate
                                 A QGIS plugin
 Selection of coordinate system
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-05-28
        copyright            : (C) 2024 by User
        email                : andreyshka3@gmail.com
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
    """Load SystemSelectCoordinate class from file SystemSelectCoordinate.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .system_select_coordinate import SystemSelectCoordinate
    return SystemSelectCoordinate(iface)
