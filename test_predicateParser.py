import unittest
from parserBase import PredicateParser # edit this to match your file name

class PredicateParserTestCase(unittest.TestCase):

    def test_id_greater_id_yes(self):#1
        t1 = ["x", ">", "y"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertTrue(pp.f)

    def test_term_id_no(self):#2
        t1 = ["x"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertFalse(pp.f)

    def test_id_plus_id_no(self):#3
        t1 = ["x", "+", "y"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertFalse(pp.f)

    def test_id_plus_id_geq_id_times_bl_id_minus_num_br_yes(self):#4
        t1 = ["x", "+", "y", ">=", "x", "*", "(", "y", "-", "3", ")"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertTrue(pp.f)

    def test_id_gr_bl_id_minus_num_br_yes(self):#5
        t1 = ["y", ">", "(", "y", "-", "3", ")"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertTrue(pp.f)

    def test_id_less_id_and_id_less_id_yes(self):#6
        t1 = ["x", "<", "y", "AND", "y", "<", "z"]#UP TO HERE IS GOOD
        pp = PredicateParser(t1)
        pp.parse()
        self.assertTrue(pp.f)

    def test_id_gr_id_and_sql_id_eq_id_or_id_eq_id_times_bl_id_plus_num_br_sqr_yes(self):#7
        t1 = ["x", ">", "y", "AND", "[", "y", "=", "z", "OR", "y", "=", "z", "*", "(", "x", "+", "1", ")", "]"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertTrue(pp.f)

    def test_forall_id_dots_sql_id_lt_num_imp_id_times_id_lt_num_sqr_yes(self):#8
        t1 = ["FORALL", "x", "::", "[", "x", "<", "5", "IMP", "x", "*", "x", "<", "25", "]"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertTrue(pp.f)

    def test_forall_id_dots_id_gt_id_yes(self):#9
        t1 = ["FORALL", "x", "::", "x", ">", "y"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertTrue(pp.f)

    def test_forall_id_dots_sql_id_AND_id_sqr_no(self):#10
        t1 = ["FORALL", "x", "::", "[", "x", "AND", "y", "]"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertFalse(pp.f)

    def test_exists_id_dots_sql_forall_id_dots_id_gt_id_sqr_yes(self):#11
        t1 = ["EXISTS", "y", "::", "[", "FORALL", "x", "::", "x", ">", "y", "]"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertTrue(pp.f)

    def test_exists_id_dots_sql_forall_id_dots_id_gt_id_no(self):#12
        t1 = ["EXISTS", "y", "::", "[", "FORALL", "x", "::", "x", ">", "y"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertFalse(pp.f)

    def test_id_plus_id_greater_id_plus_id_yes(self):#13
        t1 = ["x", "+", "y", ">", "yz", "+", "xxx"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertTrue(pp.f)

    def test_bl_id_plus_id_br_times_id_greater_id_plus_id_yes(self):#14
        t1 = ["(", "x", "+", "y", ")", "*", "z", ">", "yz", "+", "xxx"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertTrue(pp.f)

    def test_bl_id_plus_id_times_id_greater_id_plus_id_no(self):#15
        t1 = ["(", "x", "+", "y", "*", "z", ">", "yz", "+", "xxx"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertFalse(pp.f)

    def test_id_plus_bl_id_times_id_br_greater_id_plus_id_yes(self):#16
        t1 = ["x", "+", "(", "y", "*", "z", ")", ">", "yz", "+", "xxx"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertTrue(pp.f)

    def test_id_times_id_eq_id_yes(self):#17
        t1 = ["x", "*", "y", "=", "qr"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertTrue(pp.f)

    def test_id_id_no(self):#18
        t1 = ["x", "y"]
        pp = PredicateParser(t1)
        pp.parse()
        self.assertFalse(pp.f)
