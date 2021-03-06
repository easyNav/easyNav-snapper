#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of easyNav-snapper.
# https://github.com/easyNav/easyNav-snapper

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Joel Tong me@joeltong.org

from preggy import expect

from easyNav_snapper import Snapper
from tests.base import TestCase

import os

PATH = os.getcwd()


class VersionTestCase(TestCase):

    def test_can_save(self):

        s = Snapper()
        s.save(PATH + '/temp.dataset')
        pass


    def test_can_append(self):
        s = Snapper()
        record = {
            'target': 1,
            'data': {
                'fieldStrength': 20
            }
        }
        s.append(record)
        s.append(record)
        s.append(record)

        s.save('temp.dataset')

        s2 = Snapper()
        s2.load('temp.dataset')

        expect(s2.data[0].get('target')).to_equal(1)
        expect(s2.data[2].get('target')).to_equal(1)
        expect(s2.data[2].get('data').get('fieldStrength')).to_equal(20)


    def test_can_delete(self):
        s = Snapper()
        record = {
            'target': 1,
            'data': {
                'fieldStrength': 20
            }
        }
        s.append(record)
        s.append(record)
        s.append(record)

        uuidToDel = s.data[1]['uuid']

        expect(len(s.data)).to_equal(3)
        s.remove(uuidToDel)
        expect(len(s.data)).to_equal(2)


    def test_can_export(self):
        s = Snapper()
        record = {
            'target': 1,
            'data': {
                'fieldStrength': 20
            }
        }

        record2 = {
            'target': 2,
            'data': {
                'fieldStrength': 40,
                'temp': 28.8
            }
        }
        s.append(record)
        s.append(record2)
        s.append(record)

        s.export('temp.dataset.exptd')


    def test_can_train(self):
        s = Snapper()
        record = {
            'target': 1,
            'data': {
                'fieldStrength': 20
            }
        }

        record2 = {
            'target': 2,
            'data': {
                'fieldStrength': 40,
                'temp': 28.8
            }
        }
        s.append(record)
        s.append(record2)
        s.append(record)

        s.trainKNN(neighbors=3)


    def test_can_predict(self):
        s = Snapper()
        record = {
            'target': 1,
            'data': {
                'fieldStrength': 20,
                'temp': 28.8
            }
        }

        record2 = {
            'target': 2,
            'data': {
                'fieldStrength': 40,
                'temp': 28.8
            }
        }
        s.append(record)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record)

        s.trainKNN(neighbors=10)
        s.predict({
            'fieldStrength' : 25,
            'temp': 28.8
            })


    def test_svm_can_work(self):
        s = Snapper()
        record = {
            'target': 1,
            'data': {
                'fieldStrength': 20,
                'temp': 28.8
            }
        }

        record2 = {
            'target': 2,
            'data': {
                'fieldStrength': 40,
                'temp': 28.8
            }
        }
        s.append(record)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record2)
        s.append(record)

        s.trainSVM()
        prediction = s.predict({
            'fieldStrength' : 25,
            'temp': 28.8
            })

        print 'prediction: ', prediction, '-------'



    def test_stats_can_work(self):
        s = Snapper()
        s.load('easyNav_snapper/datasets/com1_2_181014_itr5.dataset')
        # s.load('easyNav_snapper/datasets/com1_2_221014_itr1.dataset')
        s.printStats()


