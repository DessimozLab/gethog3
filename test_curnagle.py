
import dill as dill_pickle
import os
import _utils
from os import listdir
import xml.etree.ElementTree as ET

from xml.dom import minidom


working_folder = "/work/FAC/FBM/DBC/cdessim2/default/smajidi1/fastget/qfo2/"
gene_trees_folder = working_folder + "/gene_trees_test/"
address_rhogs_folder = working_folder + "/rhog_size_g2_s500/"  # "/rhog_size_g2_s500/" sample_rootHOG
species_tree_address = working_folder + "lineage_tree_qfo.phyloxml"
pickle_address = working_folder + "/pickle_folder/"

pickle_files_adress = listdir(pickle_address)

HOGs_a_rhog_xml_all = []
for pickle_file_adress in pickle_files_adress:
    with open(pickle_address+ pickle_file_adress, 'rb') as handle:

        HOGs_a_rhog_xml_all += dill_pickle.load(handle)

print(HOGs_a_rhog_xml_all)

rhogid_num_list = _utils.list_rhog_fastas(address_rhogs_folder)
rhogid_num_list_input = rhogid_num_list[9:13]

(groups_xml, gene_id_name, orthoxml_file, rhogid_len_list) = _utils.prepare_xml(rhogid_num_list_input,
                                                                                address_rhogs_folder)
for HOGs_a_rhog_xml in HOGs_a_rhog_xml_all:
    groups_xml.append(HOGs_a_rhog_xml)
xml_str = minidom.parseString(ET.tostring(orthoxml_file)).toprettyxml(indent="   ")
print(xml_str)