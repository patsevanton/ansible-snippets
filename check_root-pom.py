#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import os
import sys

fn = sys.argv[1]
version = None

ns = {"pom":"http://maven.apache.org/POM/4.0.0"}
a = {"assembly", "puppet-config"}

if 'pom.xml' in fn:
    my_xml = etree.parse(fn)
    modules = my_xml.xpath("//pom:project/pom:modules", namespaces=ns)
    for module in modules:
        b = [i.text for i in module.findall("pom:module", namespaces=ns)]
        c = a.intersection(b)
        if c == a:
            parents = my_xml.xpath("//pom:project/pom:parent", namespaces=ns)
            for parent in parents:
                root_pom = parent.find("pom:artifactId", namespaces=ns).text
                version = float(parent.find("pom:version", namespaces=ns).text)
                if root_pom == "root-pom" and version == 1.15:
                    print("root-pom = 1.15")
                else:
                    print("root-pom must be = 1.15 https://confluence.tools.mycompany.ru/display/GI/CM+RoadMap")
