�PNG

   IHDR           szz�   sRGB ���  �IDATX	�W͊A5�9�%�Ir��% ����y��+x�!ă,x��9��D��Tu�j�������0Vw�WU_U��8�@�v����/����w��Yi��T*0�%�a�_��>��~�t:+��?4i�Za&��QJȸ �%�����x�t�]C��Hqw:����[�"+�J>�Nߑ�O@P�\��UR��,��� c�XB���Ɠ�D�%��c���2�4�ؗ�l@מ�f�+�~�]ϋ�F�a*��y�$0�z��n!�;�j�j��F�Zgf)<�K�6�3� �)�K �qA��N�oK������끫���qv��� �i���M�oBd�2��&�iߺ٥�,��s7�Ь8hҳu	�"�f�z��z=s��f3��K�BݰЙ�������ۘp ־����c��B@�T۱?7[���"��� *U�׭3׾8�ֳn0�J]&��F�=J�x�'�C@���d#f�X,,D�X�5�q�P����v��1]���.�����T�'�\.��V�Yg	���%��,�˥�݅BA�0��ßT�@���u��l�<3/�F,����,�>��.�J�w��W2x�'�_�V�g�;�>����;��xҧ�/����8`x�������oq�͂@��    IEND�B`�﻿/*
 Copyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.
 For licensing, see LICENSE.md or http://ckeditor.com/license
*/
(function(){CKEDITOR.plugins.add("embedsemantic",{icons:"embedsemantic",hidpi:!0,requires:"embedbase",onLoad:function(){this.registerOembedTag()},init:function(a){var b=CKEDITOR.plugins.embedBase.createWidgetBaseDefinition(a),d=b.init;CKEDITOR.tools.extend(b,{dialog:"embedBase",button:a.lang.embedbase.button,allowedContent:"oembed",requiredContent:"oembed",styleableElements:"oembed",providerUrl:new CKEDITOR.template(a.config.embed_provider||"//ckeditor.iframe.ly/api/oembed?url={url}&callback={callback}"),
init:function(){var e=this;d.call(this);this.once("ready",function(){this.data.loadOnReady&&this.loadContent(this.data.url,{callback:function(){e.setData("loadOnReady",!1);a.fire("updateSnapshot")}})})},upcast:function(a,b){if("oembed"==a.name){var c=a.children[0];if(c&&c.type==CKEDITOR.NODE_TEXT&&c.value)return b.url=c.value,b.loadOnReady=!0,c=new CKEDITOR.htmlParser.element("div"),a.replaceWith(c),c.attributes["class"]=a.attributes["class"],c}},downcast:function(a){var b=new CKEDITOR.htmlParser.element("oembed");
b.add(new CKEDITOR.htmlParser.text(this.data.url));a.attributes["class"]&&(b.attributes["class"]=a.attributes["class"]);return b}},!0);a.widgets.add("embedSemantic",b)},registerOembedTag:function(){var a=CKEDITOR.dtd,b;a.oembed={"#":1};for(b in a)a[b].div&&(a[b].oembed=1)}})})();