�PNG

   IHDR         �*Ԡ  !IDATH���_lSU�?�]n��,Z"qC"l#����	CbTL�51$&�����$��}@�F��p1��C�$Ӯ@q�lt�]�{�χ{��>x�o~���~~���w��d��J4G��@/�� �k �)�s 5<�hފ��O��3 ��c���s(�B�)~���T��x�����	aRC|5�����i�:��@��>�轇�]Y�8>'��i~{����b�b�jT���AM] "]дb[ �_��������	����{{������9�����T�X��F!�b���)��q�|�P�)>SO%��R>̑��z����́�'k�N`-�m�����a�	Etٶ�(�"f���'����bh7
oD��`kI�rz:#�I��&C��Ѿ�aY�)4��Kǒ��"-at%�2��u>=����#|���f�*��c����f6���0�A��ұ�oa4�K>��n��2�W������.b�ژ,Y�'����W$n	���A>�����A����36ڰ�l�ʬX�J��y�$;Z �c~*���Hr;j�0����iX��Q>}��MQ*5��¶�y�3��B��9LGR�i�{�/@�d��,��P�1~�(p �T��u��Ļ�T��bcׄ��橖��n�����3��w�w����̏]	R�[8~b��\	l�Y�XDGQC� ��*���k�`^[�O��3�G���"�f��]�\2�3�P;���4| �D�0G�$q����a�0ܽ�ˣ%N}�%���@,�H�E*��
I"܎ַ���*�,���?1t�#���h�Z#�Xڣ��H�U�1�bF.B�ED#���SW5�������;������ס�ɢ��i�i)����1�bD�jt��;�t�9��ܝa�^(�4�_�@�j���5l�f�й;�
Z���"��įO��,L���]�g�����W��ж�c६S�zKx �v���ţ	��<7L�GT�ŬS��&ȭ�~�v`�
��#�)`Џ?�x��'��1��xp���    IEND�B`�﻿/*
 Copyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.
 For licensing, see LICENSE.md or http://ckeditor.com/license
*/
CKEDITOR.dialog.add("sourcedialog",function(a){var b=CKEDITOR.document.getWindow().getViewPaneSize(),e=Math.min(b.width-70,800),b=b.height/1.5,d;return{title:a.lang.sourcedialog.title,minWidth:100,minHeight:100,onShow:function(){this.setValueOf("main","data",d=a.getData())},onOk:function(){function b(f,c){a.focus();a.setData(c,function(){f.hide();var b=a.createRange();b.moveToElementEditStart(a.editable());b.select()})}return function(){var a=this.getValueOf("main","data").replace(/\r/g,""),c=this;
if(a===d)return!0;setTimeout(function(){b(c,a)});return!1}}(),contents:[{id:"main",label:a.lang.sourcedialog.title,elements:[{type:"textarea",id:"data",dir:"ltr",inputStyle:"cursor:auto;width:"+e+"px;height:"+b+"px;tab-size:4;text-align:left;","class":"cke_source"}]}]}});