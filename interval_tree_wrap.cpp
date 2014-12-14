#include "interval_tree.h"

#include <boost/python.hpp>

using namespace boost::python;

BOOST_PYTHON_MODULE(interval_tree_wrap)
{
    class_<interval_tree>("interval_tree")
      .def("newNode", &interval_tree::newNode)
      .def("insert", &interval_tree::insert)
      .def("doOVerlap", &interval_tree::doOVerlap)
      .def("overlapSearch", &interval_tree::overlapSearch)
      .def("inorder", &interval_trees::inorder)
	  .def("main", &interval_trees::main)
    ;
}