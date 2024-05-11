<!DOCTYPE html>
<html lang="en-US" class="theme-">
<head data-suburl="">
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta http-equiv="x-ua-compatible" content="ie=edge">
	<title>kuku/kot: kvot - bd/json/py_star.py at master - Agit</title>
	<meta name="theme-color" content="#6cc644">
	<meta name="author" content="kuku" />
	<meta name="description" content="kot - kvot" />
	<meta name="keywords" content="go,git,self-hosted,gitea">
	<meta name="referrer" content="no-referrer" />
	<meta name="_csrf" content="lJ-471GFhMijaoklFE82kLnjIGY6MTcwNTYzODkwNzY5MzczNTQxNw" />
	<meta name="_suburl" content="" />
	
	
	

	<script>
		window.config = {
			AppVer: 'gitea模板还原\u002b138-g943c8c71f',
			AppSubUrl: '',
			StaticUrlPrefix: '',
			UseServiceWorker:  true ,
			csrf: 'lJ-471GFhMijaoklFE82kLnjIGY6MTcwNTYzODkwNzY5MzczNTQxNw',
			HighlightJS: false,
			SimpleMDE: false,
			Tribute: false,
			U2F: false,
			Heatmap: false,
			heatmapUser: null,
			NotificationSettings: {
				MinTimeout:  10000 ,
				TimeoutStep:   10000 ,
				MaxTimeout:  60000 ,
				EventSourceUpdateTime:  10000 ,
			},
			PageIsProjects: false,
      
		};
	</script>
	<link rel="icon" href="/img/favicon.svg" type="image/svg+xml">
	<link rel="alternate icon" href="/img/favicon.png" type="image/png">
	<link rel="mask-icon" href="/img/agit-safari.svg" color="#609926">
	<link rel="fluid-icon" href="/img/agit-lg.png" title="Agit">


	<link rel="stylesheet" href="/css/index.css?v=220846678a86246c9d7e7c46c21f20c2">
	<noscript>
		<style>
      .dropdown:hover > .menu { display: block; }
      .ui.secondary.menu .dropdown.item > .menu { margin-top: 0; }
		</style>
	</noscript>
	<style class="list-search-style"></style>

	
		<meta property="og:title" content="kot" />
		<meta property="og:url" content="https://agit.ai/kuku/kot" />
		
			<meta property="og:description" content="kvot" />
		
	
	<meta property="og:type" content="object" />
	
		<meta property="og:image" content="https://agit.ai/user/avatar/kuku/-1" />
	

<meta property="og:site_name" content="Agit" />


<link rel="stylesheet" href="/vendor/plugins/xterm/xterm.css?v=220846678a86246c9d7e7c46c21f20c2" />


</head>
<body>
	

	<div class="full height">
		<noscript>This website works better with JavaScript.</noscript>

		

		
			
			<div class="ui top secondary stackable main menu following bar light" style="background: #242628; height: 52px;">
				
<div class="ui container z-max" id="navbar" v-cloak style="position:fixed;">
	<div class="i-flex i-align-center i-justify-between logo-img" style="margin-right:26px;height:52px;">
		<a href="/">
			<img class="share-nav-logo" src="/img/logo/nav-logo.svg">
		</a>
		<div class="ui basic icon button mobile-only" id="navbar-expand-toggle">
			<i class="sidebar icon"></i>
		</div>
	</div>

	
		<a class="item " href="/">Home</a>
		<a class="item" href="http://help.agit.ai" id="help-header-a" target="_blank">Help</a>
		<a class="mobile-only item " href="/explore/repos">Explore</a>
		<div class="ui input d-relative navbar-search not-mobile" :class="{active:menuVisible}">
			<i class="icon iconfont icon-search"></i>
			<input v-model="searchName" placeholder="Search" type="text" autocomplete="off"  @focus="menuVisible = true">
			<div v-show="searchName.trim() && menuVisible" class="ui segment transition z-menu" @focus="menuVisible = true">
				<div class="ui list" @click="handleSearch('repos')">
					<span class="mr-md">${searchName}</span> <span class="i-text-right">Repositories</span>
				</div>
				<div class="ui list" @click="handleSearch('users')">
					<span class="mr-md">${searchName}</span> <span class="i-text-right">Users</span>
				</div>
				<div class="ui list" @click="handleSearch('organizations')">
					<span class="mr-md">${searchName}</span> <span class="i-text-right">Organizations</span>
				</div>
			</div>

		</div>
	
	

	


	

<div class="right stackable menu header-right">
	
	<div class="ui dropdown jump item poping up active visible">
		<i class="iconfont mr-3xs font-size-2xl" :class='{"icon-lang-zh2en":lan!=="en-US","icon-lang-en2zh":lan==="en-US"}'></i>
		<span id="footerLang" class="hidden">English</span>
		<i class="caret down icon font-size-sm"></i>
		<div class="menu">
			
			<span lang="en-US" class="item active selected" onclick="handleLanguage(&#34;en-US&#34;)">English</span>
			
			<span lang="zh-CN" class="item " onclick="handleLanguage(&#34;zh-CN&#34;)">简体中文</span>
			
		</div>
	</div>

	
	<a class="item" rel="nofollow" href="/user/login?redirect_to=%2fkuku%2fkot%2fsrc%2fbranch%2fmaster%2fbd%2fjson%2fpy_star.py">
		<svg viewBox="0 0 16 16" class="svg octicon-sign-in" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 2.75C2 1.784 2.784 1 3.75 1h2.5a.75.75 0 010 1.5h-2.5a.25.25 0 00-.25.25v10.5c0 .138.112.25.25.25h2.5a.75.75 0 010 1.5h-2.5A1.75 1.75 0 012 13.25V2.75zm6.56 4.5l1.97-1.97a.75.75 0 10-1.06-1.06L6.22 7.47a.75.75 0 000 1.06l3.25 3.25a.75.75 0 101.06-1.06L8.56 8.75h5.69a.75.75 0 000-1.5H8.56z"/></svg> Sign In
	</a>
</div>


</div>

			</div>
		


<div id="repoHome" class="repository file list ">
	<div class="header-wrapper">

	<div class="ui container">
		<div class="repo-header">
			<div class="ui huge breadcrumb repo-title">
				
					<div class="repo-header-icon">
	
		<svg viewBox="0 0 16 16" class="svg octicon-repo-template" width="32" height="32" aria-hidden="true"><path fill-rule="evenodd" d="M6 .75A.75.75 0 016.75 0h2.5a.75.75 0 010 1.5h-2.5A.75.75 0 016 .75zm5 0a.75.75 0 01.75-.75h1.5a.75.75 0 01.75.75v1.5a.75.75 0 01-1.5 0V1.5h-.75A.75.75 0 0111 .75zM4.992.662a.75.75 0 01-.636.848c-.436.063-.783.41-.846.846a.75.75 0 01-1.485-.212A2.501 2.501 0 014.144.025a.75.75 0 01.848.637zM2.75 4a.75.75 0 01.75.75v1.5a.75.75 0 01-1.5 0v-1.5A.75.75 0 012.75 4zm10.5 0a.75.75 0 01.75.75v1.5a.75.75 0 01-1.5 0v-1.5a.75.75 0 01.75-.75zM2.75 8a.75.75 0 01.75.75v.268A1.72 1.72 0 013.75 9h.5a.75.75 0 010 1.5h-.5a.25.25 0 00-.25.25v.75c0 .28.114.532.3.714a.75.75 0 01-1.05 1.072A2.495 2.495 0 012 11.5V8.75A.75.75 0 012.75 8zm10.5 0a.75.75 0 01.75.75v4.5a.75.75 0 01-.75.75h-2.5a.75.75 0 010-1.5h1.75v-2h-.75a.75.75 0 010-1.5h.75v-.25a.75.75 0 01.75-.75zM6 9.75A.75.75 0 016.75 9h2.5a.75.75 0 010 1.5h-2.5A.75.75 0 016 9.75zm-1 2.5v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"/></svg>
	
</div>

				
				<a href="/kuku">kuku</a>
				<div class="divider"> / </div>
				<a href="/kuku/kot">kot</a>

				<i class="iconfont icon-ai"></i>

				
					
						
					
				
				
				
				
				
			</div>
			
				<div class="repo-buttons">
					<form method="post" action="/kuku/kot/action/watch?redirect_to=%2fkuku%2fkot%2fsrc%2fbranch%2fmaster%2fbd%2fjson%2fpy_star.py">
						<input type="hidden" name="_csrf" value="lJ-471GFhMijaoklFE82kLnjIGY6MTcwNTYzODkwNzY5MzczNTQxNw">
						<div class="ui labeled button poping up" tabindex="0" data-content="Sign in to watch this repository." data-position="top center" data-variation="tiny">
							<button type="submit" class="ui compact basic button" disabled>
								<i class="iconfont mr-2xs icon-eye"></i>Watch
							</button>
							<a class="ui basic label" href="/kuku/kot/watchers">
								1
							</a>
						</div>
					</form>
					<form method="post" action="/kuku/kot/action/star?redirect_to=%2fkuku%2fkot%2fsrc%2fbranch%2fmaster%2fbd%2fjson%2fpy_star.py">
						<input type="hidden" name="_csrf" value="lJ-471GFhMijaoklFE82kLnjIGY6MTcwNTYzODkwNzY5MzczNTQxNw">
						<div class="ui labeled button poping up" tabindex="0" data-content="Sign in to star this repository." data-position="top center" data-variation="tiny">
							<button type="submit" class="ui compact basic button" disabled>
								<i class="mr-2xs iconfont icon-star"></i>Star
							</button>
							<a class="ui basic label" href="/kuku/kot/stars">
								1
							</a>
						</div>
					</form>
					
						<div class="ui labeled button " tabindex="0">
							<a class="ui compact basic button
								poping up"
								 data-content="Sign in to fork this repository." rel="nofollow"
									href="/user/login?redirect_to=/repo/fork/2505"
								 data-position="top center" data-variation="tiny">
								<i class="mr-2xs iconfont icon-fork"></i>Fork
							</a>
							<a class="ui basic label" href="/kuku/kot/forks">
								0
							</a>
						</div>
					
				</div>
			
		</div>
	</div>

	<div class="ui tabs container">
		
			<div class="ui tabular stackable menu navbar">
				
				<a class="active item" href="/kuku/kot">
					<i class="iconfont icon-code"></i> Code
				</a>
				

				
					<a class=" item" href="/kuku/kot/issues">
						<i class="iconfont icon-open"></i> Issues <span class="ui gray tiny label circular">0</span>
					</a>
				

				

				
					<a class=" item" href="/kuku/kot/pulls">
						<i class="iconfont icon-merge-request"></i> Pull Requests <span class="ui gray tiny label circular">0</span>
					</a>
				

				
					<a class=" item" href="/kuku/kot/wiki" >
						<i class="iconfont icon-wiki"></i> Wiki
					</a>
				

				
					<a class=" item" href="/kuku/kot/activity">
						<i class="iconfont icon-activity"></i> Activity
					</a>
				

				


				
			</div>
		
	</div>
	<div class="ui tabs divider"></div>
</div>

	<span class="repo-url hidden">/kuku/kot</span>
	<span class="repo-id hidden">2505</span>
	<div class="ui container">
		



		<div class="ui repo-description">
			<div id="repo-desc">
				
					<span class="description">kvot</span>
				
				<a class="link" href=""></a>
			</div>
			
		</div>
		<div class="ui" id="repo-topics">
		
		
		</div>
		
		<div class="hide" id="validate_prompt">
			<span id="count_prompt">You can not select more than 25 topics</span>
			<span id="format_prompt">Topics must start with a letter or number, can include dashes (&#39;-&#39;) and can be up to 35 characters long.</span>
		</div>
		
		
		

		<div class="ui segments repository-summary shadow-0 is-lang-stats">
	<div class="ui segment sub-menu repository-menu">
		<div class="ui two horizontal center link list">
			
				<div class="item">
					<a class="ui" href="/kuku/kot/commits/branch/master"><i class="iconfont icon-commit"></i> <b>1626</b> Commits</a>
				</div>
			
			
				<div class="item">
					<a class="ui" href="/kuku/kot/branches/"><i class="iconfont icon-branch-down"></i> <b>1</b> Branch</a>
				</div>
				<div class="item">
					<span class="ui"><i class="iconfont icon-memory"></i> <b id="RepoSize">78 MB</b></span>
				</div>
			
		</div>
	</div>
	
	<div class="ui segment sub-menu language-stats-details" style="display: none">
		<div class="ui horizontal center link list">
			
			<div class="item">
				<span class="ui">
				<i class="color-icon" style="background-color: #f1e05a"></i>
				<b>
					JavaScript
				
				</b> 56.8%</span>
			</div>
			
			<div class="item">
				<span class="ui">
				<i class="color-icon" style="background-color: #3572A5"></i>
				<b>
					Python
				
				</b> 43.2%</span>
			</div>
			
		</div>
	</div>
	<a class="ui segment language-stats">
		
		<div class="bar" style="width: 56.8%; background-color: #f1e05a">&nbsp;</div>
		
		<div class="bar" style="width: 43.2%; background-color: #3572A5">&nbsp;</div>
		
	</a>
	
</div>

		<div class="ui stackable secondary menu mobile--margin-between-items mobile--no-negative-margins">
			<div class="fitted item choose reference">
	<div class="ui floating filter dropdown custom" data-can-create-branch="false" data-no-results="No results found.">
		<div id="branchSelect" class="ui basic small compact button" data-mode="branches" @click="menuVisible = !menuVisible" @keyup.enter="menuVisible = !menuVisible">
			<span class="text">
				<i class="iconfont icon-branch-down"></i>
				Branch:
				<strong>master</strong>
			</span>
			<i class="dropdown icon"></i>
		</div>
		<div class="data" style="display: none" data-mode="branches">
			
				<div class="item branch selected" data-url="/kuku/kot/src/branch/master/bd/json/py_star.py">master</div>
			
			
		</div>
		<div class="menu transition" :class="{visible: menuVisible}" v-if="menuVisible" v-cloak>
			<div class="ui icon search input">
				<i class="filter icon"></i>
				<input name="search" ref="searchField" v-model="searchTerm" @keydown="keydown($event)" placeholder="Filter branch or tag...">
			</div>
			<div class="header branch-tag-choice">
				<div class="ui grid">
					<div class="two column row">
						<a class="reference column" href="#" @click="mode = 'branches'; focusSearchField()">
							<span class="text" :class="{black: mode !== 'branches'}">
								<i class="iconfont icon-branch-down"></i> Branches
							</span>
						</a>
						<a class="reference column" href="#" @click="mode = 'tags'; focusSearchField()">
							<span class="text" :class="{black: mode !== 'tags'}">
								<i class="reference tags icon"></i> Tags
							</span>
						</a>
					</div>
				</div>
			</div>
			<div class="scrolling menu" ref="scrollContainer">
				<div v-for="(item, index) in filteredItems" :key="item.name" class="item" :class="{selected: item.selected, active: active == index}" @click="selectItem(item)" :ref="'listItem' + index">${ item.name }</div>
				<div class="item" v-if="showCreateNewBranch" :class="{active: active == filteredItems.length}" :ref="'listItem' + filteredItems.length">
					<a href="#" @click="createNewBranch()">
						<div>
							<i class="iconfont icon-branch-down"></i>
							Create branch <strong>${ searchTerm }</strong>
						</div>
						<div class="text small">
							
								from &#39;master&#39;
							
						</div>
					</a>
					<form ref="newBranchForm" action="/kuku/kot/branches/_new/branch/master" method="post">
						<input type="hidden" name="_csrf" value="lJ-471GFhMijaoklFE82kLnjIGY6MTcwNTYzODkwNzY5MzczNTQxNw">
						<input type="hidden" name="new_branch_name" v-model="searchTerm">
					</form>
				</div>
			</div>
			<div class="message" v-if="showNoResults">${ noResults }</div>
		</div>
	</div>
</div>

			
			
			
			
				<div class="fitted item">
					<span class="ui breadcrumb repo-path">
						<a class="section" href="/kuku/kot/src/branch/master" title="kot">kot</a>
						
							<span class="divider">/</span>
							
								<span class="section">
									<a href="/kuku/kot/src/branch/master/bd" title="bd">bd</a></span>
						
							<span class="divider">/</span>
							
								<span class="section">
									<a href="/kuku/kot/src/branch/master/bd/json" title="json">json</a></span>
						
							<span class="divider">/</span>
							
								<span class="active section" title="py_star.py">py_star.py</span>
							
						</span></div>
			
			<div class="right fitted item" id="file-buttons">
				<div>
					
						
						
					

					
					
				</div>
			</div>

			<div class="fitted item">
				
				
			</div>
		</div>
		
			<div class="tab-size-8 non-diff-file-content">
	<h4 class="file-header ui top attached header">
		<div class="file-header-left df ac">
			
				<div class="file-info text grey normal mono">
					
					
						<div class="file-info-entry">
							156 lines
						</div>
					
					
						<div class="file-info-entry">
							14 KB
						</div>
					
					
				</div>
			
		</div>
		
		<div class="file-header-right df ac">
			<div class="ui right file-actions">
				<div class="ui buttons">
					<a class="ui button" href="/kuku/kot/raw/branch/master/bd/json/py_star.py">Raw</a>
					
						<a class="ui button" href="/kuku/kot/src/commit/a3d34081452f9537cdb77a95883fba9fb209db5c/bd/json/py_star.py">Permalink</a>
					
					
						<a class="ui button" href="/kuku/kot/blame/branch/master/bd/json/py_star.py">Blame</a>
					
					<a class="ui button" href="/kuku/kot/commits/branch/master/bd/json/py_star.py">History</a>
				</div>
				
					
						<span class="btn-octicon poping up disabled" data-content="You must fork this repository to make or propose changes to this file." data-position="bottom center" data-variation="tiny inverted"><svg viewBox="0 0 16 16" class="svg octicon-pencil" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11.013 1.427a1.75 1.75 0 012.474 0l1.086 1.086a1.75 1.75 0 010 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 01-.927-.928l.929-3.25a1.75 1.75 0 01.445-.758l8.61-8.61zm1.414 1.06a.25.25 0 00-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 000-.354l-1.086-1.086zM11.189 6.25L9.75 4.81l-6.286 6.287a.25.25 0 00-.064.108l-.558 1.953 1.953-.558a.249.249 0 00.108-.064l6.286-6.286z"/></svg></span>
					
					
						<span class="btn-octicon poping up disabled" data-content="You must have write access to make or propose changes to this file." data-position="bottom center" data-variation="tiny inverted"><svg viewBox="0 0 16 16" class="svg octicon-trashcan" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z"/></svg></span>
					
				
			</div>
		</div>
		
	</h4>
	<div class="ui attached table unstackable segment">
		<div class="file-view code-view">
			
				
				<table>
					<tbody>
						
						<tr>
							<td id="L1" class="lines-num">
								<span id="L1" data-line-number="1"></span>
							</td>
							<td rel="L1" class="lines-code chroma">
								<code><span class="kn">import</span> <span class="nn">sys</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L2" class="lines-num">
								<span id="L2" data-line-number="2"></span>
							</td>
							<td rel="L2" class="lines-code chroma">
								<code><span class="n">sys</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">..</span><span class="s1">&#39;</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L3" class="lines-num">
								<span id="L3" data-line-number="3"></span>
							</td>
							<td rel="L3" class="lines-code chroma">
								<code><span class="kn">from</span> <span class="nn">base.spider</span> <span class="kn">import</span> <span class="n">Spider</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L4" class="lines-num">
								<span id="L4" data-line-number="4"></span>
							</td>
							<td rel="L4" class="lines-code chroma">
								<code><span class="kn">import</span> <span class="nn">json</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L5" class="lines-num">
								<span id="L5" data-line-number="5"></span>
							</td>
							<td rel="L5" class="lines-code chroma">
								<code>
</code>
							</td>
						</tr>
						
						<tr>
							<td id="L6" class="lines-num">
								<span id="L6" data-line-number="6"></span>
							</td>
							<td rel="L6" class="lines-code chroma">
								<code><span class="k">class</span> <span class="nc">Spider</span><span class="p">(</span><span class="n">Spider</span><span class="p">)</span><span class="p">:</span>  <span class="c1"># 元类 默认的元类 type</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L7" class="lines-num">
								<span id="L7" data-line-number="7"></span>
							</td>
							<td rel="L7" class="lines-code chroma">
								<code>    <span class="k">def</span> <span class="nf">getName</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L8" class="lines-num">
								<span id="L8" data-line-number="8"></span>
							</td>
							<td rel="L8" class="lines-code chroma">
								<code>        <span class="k">return</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">星光影视</span><span class="s2">&#34;</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L9" class="lines-num">
								<span id="L9" data-line-number="9"></span>
							</td>
							<td rel="L9" class="lines-code chroma">
								<code>    <span class="k">def</span> <span class="nf">init</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">extend</span><span class="o">=</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L10" class="lines-num">
								<span id="L10" data-line-number="10"></span>
							</td>
							<td rel="L10" class="lines-code chroma">
								<code>        <span class="k">print</span><span class="p">(</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">============{0}============</span><span class="s2">&#34;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">extend</span><span class="p">)</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L11" class="lines-num">
								<span id="L11" data-line-number="11"></span>
							</td>
							<td rel="L11" class="lines-code chroma">
								<code>        <span class="k">pass</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L12" class="lines-num">
								<span id="L12" data-line-number="12"></span>
							</td>
							<td rel="L12" class="lines-code chroma">
								<code>    <span class="k">def</span> <span class="nf">homeContent</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="nb">filter</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L13" class="lines-num">
								<span id="L13" data-line-number="13"></span>
							</td>
							<td rel="L13" class="lines-code chroma">
								<code>        <span class="n">result</span> <span class="o">=</span> <span class="p">{</span><span class="p">}</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L14" class="lines-num">
								<span id="L14" data-line-number="14"></span>
							</td>
							<td rel="L14" class="lines-code chroma">
								<code>        <span class="n">cateManual</span> <span class="o">=</span> <span class="p">{</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L15" class="lines-num">
								<span id="L15" data-line-number="15"></span>
							</td>
							<td rel="L15" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">电影</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">电影</span><span class="s2">&#34;</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L16" class="lines-num">
								<span id="L16" data-line-number="16"></span>
							</td>
							<td rel="L16" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">电视剧</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">电视剧</span><span class="s2">&#34;</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L17" class="lines-num">
								<span id="L17" data-line-number="17"></span>
							</td>
							<td rel="L17" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">动漫</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">动漫</span><span class="s2">&#34;</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L18" class="lines-num">
								<span id="L18" data-line-number="18"></span>
							</td>
							<td rel="L18" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">综艺</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">综艺</span><span class="s2">&#34;</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L19" class="lines-num">
								<span id="L19" data-line-number="19"></span>
							</td>
							<td rel="L19" class="lines-code chroma">
								<code>        <span class="p">}</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L20" class="lines-num">
								<span id="L20" data-line-number="20"></span>
							</td>
							<td rel="L20" class="lines-code chroma">
								<code>        <span class="n">classes</span> <span class="o">=</span> <span class="p">[</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L21" class="lines-num">
								<span id="L21" data-line-number="21"></span>
							</td>
							<td rel="L21" class="lines-code chroma">
								<code>        <span class="k">for</span> <span class="n">k</span> <span class="ow">in</span> <span class="n">cateManual</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L22" class="lines-num">
								<span id="L22" data-line-number="22"></span>
							</td>
							<td rel="L22" class="lines-code chroma">
								<code>            <span class="n">classes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="p">{</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L23" class="lines-num">
								<span id="L23" data-line-number="23"></span>
							</td>
							<td rel="L23" class="lines-code chroma">
								<code>                <span class="sa"></span><span class="s1">&#39;</span><span class="s1">type_name</span><span class="s1">&#39;</span><span class="p">:</span><span class="n">k</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L24" class="lines-num">
								<span id="L24" data-line-number="24"></span>
							</td>
							<td rel="L24" class="lines-code chroma">
								<code>                <span class="sa"></span><span class="s1">&#39;</span><span class="s1">type_id</span><span class="s1">&#39;</span><span class="p">:</span><span class="n">cateManual</span><span class="p">[</span><span class="n">k</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L25" class="lines-num">
								<span id="L25" data-line-number="25"></span>
							</td>
							<td rel="L25" class="lines-code chroma">
								<code>            <span class="p">}</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L26" class="lines-num">
								<span id="L26" data-line-number="26"></span>
							</td>
							<td rel="L26" class="lines-code chroma">
								<code>
</code>
							</td>
						</tr>
						
						<tr>
							<td id="L27" class="lines-num">
								<span id="L27" data-line-number="27"></span>
							</td>
							<td rel="L27" class="lines-code chroma">
								<code>        <span class="n">result</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">class</span><span class="s1">&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">classes</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L28" class="lines-num">
								<span id="L28" data-line-number="28"></span>
							</td>
							<td rel="L28" class="lines-code chroma">
								<code>        <span class="k">if</span><span class="p">(</span><span class="nb">filter</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L29" class="lines-num">
								<span id="L29" data-line-number="29"></span>
							</td>
							<td rel="L29" class="lines-code chroma">
								<code>            <span class="n">result</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">filters</span><span class="s1">&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">filter</span><span class="s1">&#39;</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L30" class="lines-num">
								<span id="L30" data-line-number="30"></span>
							</td>
							<td rel="L30" class="lines-code chroma">
								<code>        <span class="k">return</span> <span class="n">result</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L31" class="lines-num">
								<span id="L31" data-line-number="31"></span>
							</td>
							<td rel="L31" class="lines-code chroma">
								<code>    <span class="k">def</span> <span class="nf">homeVideoContent</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L32" class="lines-num">
								<span id="L32" data-line-number="32"></span>
							</td>
							<td rel="L32" class="lines-code chroma">
								<code>        <span class="n">rsp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fetch</span><span class="p">(</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">http://43.155.75.36:1069/api.php?do=index_list</span><span class="s2">&#34;</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L33" class="lines-num">
								<span id="L33" data-line-number="33"></span>
							</td>
							<td rel="L33" class="lines-code chroma">
								<code>        <span class="n">alist</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">rsp</span><span class="o">.</span><span class="n">text</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L34" class="lines-num">
								<span id="L34" data-line-number="34"></span>
							</td>
							<td rel="L34" class="lines-code chroma">
								<code>        <span class="n">alist</span> <span class="o">=</span> <span class="n">alist</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">list</span><span class="s1">&#39;</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L35" class="lines-num">
								<span id="L35" data-line-number="35"></span>
							</td>
							<td rel="L35" class="lines-code chroma">
								<code>        <span class="n">videos</span> <span class="o">=</span> <span class="p">[</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L36" class="lines-num">
								<span id="L36" data-line-number="36"></span>
							</td>
							<td rel="L36" class="lines-code chroma">
								<code>
</code>
							</td>
						</tr>
						
						<tr>
							<td id="L37" class="lines-num">
								<span id="L37" data-line-number="37"></span>
							</td>
							<td rel="L37" class="lines-code chroma">
								<code>        <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">alist</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L38" class="lines-num">
								<span id="L38" data-line-number="38"></span>
							</td>
							<td rel="L38" class="lines-code chroma">
								<code>            <span class="n">videos</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="p">{</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L39" class="lines-num">
								<span id="L39" data-line-number="39"></span>
							</td>
							<td rel="L39" class="lines-code chroma">
								<code>                <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_id</span><span class="s2">&#34;</span><span class="p">:</span><span class="n">a</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">id</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L40" class="lines-num">
								<span id="L40" data-line-number="40"></span>
							</td>
							<td rel="L40" class="lines-code chroma">
								<code>                <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_name</span><span class="s2">&#34;</span><span class="p">:</span><span class="n">a</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">name</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L41" class="lines-num">
								<span id="L41" data-line-number="41"></span>
							</td>
							<td rel="L41" class="lines-code chroma">
								<code>                <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_pic</span><span class="s2">&#34;</span><span class="p">:</span><span class="n">a</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">pic</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L42" class="lines-num">
								<span id="L42" data-line-number="42"></span>
							</td>
							<td rel="L42" class="lines-code chroma">
								<code>                <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_remarks</span><span class="s2">&#34;</span><span class="p">:</span><span class="n">a</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">text</span><span class="s1">&#39;</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L43" class="lines-num">
								<span id="L43" data-line-number="43"></span>
							</td>
							<td rel="L43" class="lines-code chroma">
								<code>            <span class="p">}</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L44" class="lines-num">
								<span id="L44" data-line-number="44"></span>
							</td>
							<td rel="L44" class="lines-code chroma">
								<code>        <span class="n">result</span> <span class="o">=</span> <span class="p">{</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L45" class="lines-num">
								<span id="L45" data-line-number="45"></span>
							</td>
							<td rel="L45" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s1">&#39;</span><span class="s1">list</span><span class="s1">&#39;</span><span class="p">:</span><span class="n">videos</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L46" class="lines-num">
								<span id="L46" data-line-number="46"></span>
							</td>
							<td rel="L46" class="lines-code chroma">
								<code>        <span class="p">}</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L47" class="lines-num">
								<span id="L47" data-line-number="47"></span>
							</td>
							<td rel="L47" class="lines-code chroma">
								<code>        <span class="k">return</span> <span class="n">result</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L48" class="lines-num">
								<span id="L48" data-line-number="48"></span>
							</td>
							<td rel="L48" class="lines-code chroma">
								<code>    <span class="k">def</span> <span class="nf">categoryContent</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">tid</span><span class="p">,</span><span class="n">pg</span><span class="p">,</span><span class="nb">filter</span><span class="p">,</span><span class="n">extend</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L49" class="lines-num">
								<span id="L49" data-line-number="49"></span>
							</td>
							<td rel="L49" class="lines-code chroma">
								<code>        <span class="n">result</span> <span class="o">=</span> <span class="p">{</span><span class="p">}</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L50" class="lines-num">
								<span id="L50" data-line-number="50"></span>
							</td>
							<td rel="L50" class="lines-code chroma">
								<code>        <span class="k">if</span> <span class="sa"></span><span class="s1">&#39;</span><span class="s1">name</span><span class="s1">&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">extend</span><span class="o">.</span><span class="n">keys</span><span class="p">(</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L51" class="lines-num">
								<span id="L51" data-line-number="51"></span>
							</td>
							<td rel="L51" class="lines-code chroma">
								<code>            <span class="n">extend</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">name</span><span class="s1">&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">tid</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L52" class="lines-num">
								<span id="L52" data-line-number="52"></span>
							</td>
							<td rel="L52" class="lines-code chroma">
								<code>        <span class="n">extend</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">page</span><span class="s1">&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">pg</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L53" class="lines-num">
								<span id="L53" data-line-number="53"></span>
							</td>
							<td rel="L53" class="lines-code chroma">
								<code>        <span class="n">filterParams</span> <span class="o">=</span> <span class="p">[</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">area</span><span class="s2">&#34;</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">by</span><span class="s2">&#34;</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">lang</span><span class="s2">&#34;</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">p</span><span class="s2">&#34;</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">year</span><span class="s2">&#34;</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L54" class="lines-num">
								<span id="L54" data-line-number="54"></span>
							</td>
							<td rel="L54" class="lines-code chroma">
								<code>        <span class="n">params</span> <span class="o">=</span> <span class="p">[</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L55" class="lines-num">
								<span id="L55" data-line-number="55"></span>
							</td>
							<td rel="L55" class="lines-code chroma">
								<code>        <span class="k">for</span> <span class="n">idx</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">filterParams</span><span class="p">)</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L56" class="lines-num">
								<span id="L56" data-line-number="56"></span>
							</td>
							<td rel="L56" class="lines-code chroma">
								<code>            <span class="n">fp</span> <span class="o">=</span> <span class="n">filterParams</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L57" class="lines-num">
								<span id="L57" data-line-number="57"></span>
							</td>
							<td rel="L57" class="lines-code chroma">
								<code>            <span class="k">if</span> <span class="n">fp</span> <span class="ow">in</span> <span class="n">extend</span><span class="o">.</span><span class="n">keys</span><span class="p">(</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L58" class="lines-num">
								<span id="L58" data-line-number="58"></span>
							</td>
							<td rel="L58" class="lines-code chroma">
								<code>
</code>
							</td>
						</tr>
						
						<tr>
							<td id="L59" class="lines-num">
								<span id="L59" data-line-number="59"></span>
							</td>
							<td rel="L59" class="lines-code chroma">
								<code>                <span class="n">params</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">fp</span> <span class="o">+</span> <span class="sa"></span><span class="s1">&#39;</span><span class="s1">=</span><span class="s1">&#39;</span> <span class="o">+</span>  <span class="n">extend</span><span class="p">[</span><span class="n">fp</span><span class="p">]</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L60" class="lines-num">
								<span id="L60" data-line-number="60"></span>
							</td>
							<td rel="L60" class="lines-code chroma">
								<code>        <span class="n">suffix</span> <span class="o">=</span> <span class="sa"></span><span class="s1">&#39;</span><span class="s1">&amp;</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">params</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L61" class="lines-num">
								<span id="L61" data-line-number="61"></span>
							</td>
							<td rel="L61" class="lines-code chroma">
								<code>        <span class="n">url</span> <span class="o">=</span> <span class="sa"></span><span class="s1">&#39;</span><span class="s1">http://43.155.75.36:1069/api.php?do=class_list&amp;{0}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">suffix</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L62" class="lines-num">
								<span id="L62" data-line-number="62"></span>
							</td>
							<td rel="L62" class="lines-code chroma">
								<code>        <span class="n">rsp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fetch</span><span class="p">(</span><span class="n">url</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L63" class="lines-num">
								<span id="L63" data-line-number="63"></span>
							</td>
							<td rel="L63" class="lines-code chroma">
								<code>        <span class="n">alists</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">rsp</span><span class="o">.</span><span class="n">text</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L64" class="lines-num">
								<span id="L64" data-line-number="64"></span>
							</td>
							<td rel="L64" class="lines-code chroma">
								<code>        <span class="n">alist</span> <span class="o">=</span> <span class="n">alists</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">list</span><span class="s1">&#39;</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L65" class="lines-num">
								<span id="L65" data-line-number="65"></span>
							</td>
							<td rel="L65" class="lines-code chroma">
								<code>        <span class="n">videos</span> <span class="o">=</span> <span class="p">[</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L66" class="lines-num">
								<span id="L66" data-line-number="66"></span>
							</td>
							<td rel="L66" class="lines-code chroma">
								<code>        <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">alist</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L67" class="lines-num">
								<span id="L67" data-line-number="67"></span>
							</td>
							<td rel="L67" class="lines-code chroma">
								<code>            <span class="n">videos</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="p">{</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L68" class="lines-num">
								<span id="L68" data-line-number="68"></span>
							</td>
							<td rel="L68" class="lines-code chroma">
								<code>                <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_id</span><span class="s2">&#34;</span><span class="p">:</span><span class="n">a</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">id</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L69" class="lines-num">
								<span id="L69" data-line-number="69"></span>
							</td>
							<td rel="L69" class="lines-code chroma">
								<code>                <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_name</span><span class="s2">&#34;</span><span class="p">:</span><span class="n">a</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">name</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L70" class="lines-num">
								<span id="L70" data-line-number="70"></span>
							</td>
							<td rel="L70" class="lines-code chroma">
								<code>                <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_pic</span><span class="s2">&#34;</span><span class="p">:</span><span class="n">a</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">pic</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L71" class="lines-num">
								<span id="L71" data-line-number="71"></span>
							</td>
							<td rel="L71" class="lines-code chroma">
								<code>                <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_remarks</span><span class="s2">&#34;</span><span class="p">:</span><span class="n">a</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">progress</span><span class="s1">&#39;</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L72" class="lines-num">
								<span id="L72" data-line-number="72"></span>
							</td>
							<td rel="L72" class="lines-code chroma">
								<code>            <span class="p">}</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L73" class="lines-num">
								<span id="L73" data-line-number="73"></span>
							</td>
							<td rel="L73" class="lines-code chroma">
								<code>
</code>
							</td>
						</tr>
						
						<tr>
							<td id="L74" class="lines-num">
								<span id="L74" data-line-number="74"></span>
							</td>
							<td rel="L74" class="lines-code chroma">
								<code>        <span class="n">result</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">list</span><span class="s1">&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">videos</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L75" class="lines-num">
								<span id="L75" data-line-number="75"></span>
							</td>
							<td rel="L75" class="lines-code chroma">
								<code>        <span class="n">result</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">page</span><span class="s1">&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">pg</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L76" class="lines-num">
								<span id="L76" data-line-number="76"></span>
							</td>
							<td rel="L76" class="lines-code chroma">
								<code>        <span class="n">result</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">pagecount</span><span class="s1">&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">9999</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L77" class="lines-num">
								<span id="L77" data-line-number="77"></span>
							</td>
							<td rel="L77" class="lines-code chroma">
								<code>        <span class="n">result</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">limit</span><span class="s1">&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">90</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L78" class="lines-num">
								<span id="L78" data-line-number="78"></span>
							</td>
							<td rel="L78" class="lines-code chroma">
								<code>        <span class="n">result</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">total</span><span class="s1">&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">999999</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L79" class="lines-num">
								<span id="L79" data-line-number="79"></span>
							</td>
							<td rel="L79" class="lines-code chroma">
								<code>        <span class="k">return</span> <span class="n">result</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L80" class="lines-num">
								<span id="L80" data-line-number="80"></span>
							</td>
							<td rel="L80" class="lines-code chroma">
								<code>    <span class="k">def</span> <span class="nf">detailContent</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">array</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L81" class="lines-num">
								<span id="L81" data-line-number="81"></span>
							</td>
							<td rel="L81" class="lines-code chroma">
								<code>        <span class="n">tid</span> <span class="o">=</span> <span class="n">array</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L82" class="lines-num">
								<span id="L82" data-line-number="82"></span>
							</td>
							<td rel="L82" class="lines-code chroma">
								<code>        <span class="n">url</span> <span class="o">=</span> <span class="sa"></span><span class="s1">&#39;</span><span class="s1">http://43.155.75.36:1069/api.php?do=detail_info&amp;id={0}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">tid</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L83" class="lines-num">
								<span id="L83" data-line-number="83"></span>
							</td>
							<td rel="L83" class="lines-code chroma">
								<code>        <span class="n">rsp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fetch</span><span class="p">(</span><span class="n">url</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L84" class="lines-num">
								<span id="L84" data-line-number="84"></span>
							</td>
							<td rel="L84" class="lines-code chroma">
								<code>        <span class="n">alists</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">rsp</span><span class="o">.</span><span class="n">text</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L85" class="lines-num">
								<span id="L85" data-line-number="85"></span>
							</td>
							<td rel="L85" class="lines-code chroma">
								<code>        <span class="n">alist</span> <span class="o">=</span> <span class="n">alists</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">info</span><span class="s1">&#39;</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L86" class="lines-num">
								<span id="L86" data-line-number="86"></span>
							</td>
							<td rel="L86" class="lines-code chroma">
								<code>        <span class="n">vod</span> <span class="o">=</span> <span class="p">{</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L87" class="lines-num">
								<span id="L87" data-line-number="87"></span>
							</td>
							<td rel="L87" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_id</span><span class="s2">&#34;</span><span class="p">:</span> <span class="n">alist</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">id</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L88" class="lines-num">
								<span id="L88" data-line-number="88"></span>
							</td>
							<td rel="L88" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_name</span><span class="s2">&#34;</span><span class="p">:</span> <span class="n">alist</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">name</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L89" class="lines-num">
								<span id="L89" data-line-number="89"></span>
							</td>
							<td rel="L89" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_pic</span><span class="s2">&#34;</span><span class="p">:</span> <span class="n">alist</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">pic</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L90" class="lines-num">
								<span id="L90" data-line-number="90"></span>
							</td>
							<td rel="L90" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">type_name</span><span class="s2">&#34;</span><span class="p">:</span> <span class="n">alist</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">vclass</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L91" class="lines-num">
								<span id="L91" data-line-number="91"></span>
							</td>
							<td rel="L91" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_year</span><span class="s2">&#34;</span><span class="p">:</span> <span class="n">alist</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">year</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L92" class="lines-num">
								<span id="L92" data-line-number="92"></span>
							</td>
							<td rel="L92" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_area</span><span class="s2">&#34;</span><span class="p">:</span> <span class="n">alist</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">area</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L93" class="lines-num">
								<span id="L93" data-line-number="93"></span>
							</td>
							<td rel="L93" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_remarks</span><span class="s2">&#34;</span><span class="p">:</span> <span class="n">alist</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">progress</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L94" class="lines-num">
								<span id="L94" data-line-number="94"></span>
							</td>
							<td rel="L94" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_actor</span><span class="s2">&#34;</span><span class="p">:</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L95" class="lines-num">
								<span id="L95" data-line-number="95"></span>
							</td>
							<td rel="L95" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_director</span><span class="s2">&#34;</span><span class="p">:</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L96" class="lines-num">
								<span id="L96" data-line-number="96"></span>
							</td>
							<td rel="L96" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_play_from</span><span class="s2">&#34;</span><span class="p">:</span><span class="n">alist</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">form</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L97" class="lines-num">
								<span id="L97" data-line-number="97"></span>
							</td>
							<td rel="L97" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_play_url</span><span class="s2">&#34;</span><span class="p">:</span><span class="n">alist</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">playurl</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L98" class="lines-num">
								<span id="L98" data-line-number="98"></span>
							</td>
							<td rel="L98" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_content</span><span class="s2">&#34;</span><span class="p">:</span> <span class="n">alist</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">introduce</span><span class="s1">&#39;</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L99" class="lines-num">
								<span id="L99" data-line-number="99"></span>
							</td>
							<td rel="L99" class="lines-code chroma">
								<code>        <span class="p">}</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L100" class="lines-num">
								<span id="L100" data-line-number="100"></span>
							</td>
							<td rel="L100" class="lines-code chroma">
								<code>
</code>
							</td>
						</tr>
						
						<tr>
							<td id="L101" class="lines-num">
								<span id="L101" data-line-number="101"></span>
							</td>
							<td rel="L101" class="lines-code chroma">
								<code>        <span class="n">result</span> <span class="o">=</span> <span class="p">{</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L102" class="lines-num">
								<span id="L102" data-line-number="102"></span>
							</td>
							<td rel="L102" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s1">&#39;</span><span class="s1">list</span><span class="s1">&#39;</span><span class="p">:</span><span class="p">[</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L103" class="lines-num">
								<span id="L103" data-line-number="103"></span>
							</td>
							<td rel="L103" class="lines-code chroma">
								<code>                <span class="n">vod</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L104" class="lines-num">
								<span id="L104" data-line-number="104"></span>
							</td>
							<td rel="L104" class="lines-code chroma">
								<code>            <span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L105" class="lines-num">
								<span id="L105" data-line-number="105"></span>
							</td>
							<td rel="L105" class="lines-code chroma">
								<code>        <span class="p">}</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L106" class="lines-num">
								<span id="L106" data-line-number="106"></span>
							</td>
							<td rel="L106" class="lines-code chroma">
								<code>        <span class="k">return</span> <span class="n">result</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L107" class="lines-num">
								<span id="L107" data-line-number="107"></span>
							</td>
							<td rel="L107" class="lines-code chroma">
								<code>
</code>
							</td>
						</tr>
						
						<tr>
							<td id="L108" class="lines-num">
								<span id="L108" data-line-number="108"></span>
							</td>
							<td rel="L108" class="lines-code chroma">
								<code>    <span class="k">def</span> <span class="nf">searchContent</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">key</span><span class="p">,</span><span class="n">quick</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L109" class="lines-num">
								<span id="L109" data-line-number="109"></span>
							</td>
							<td rel="L109" class="lines-code chroma">
								<code>        <span class="n">url</span> <span class="o">=</span> <span class="sa"></span><span class="s1">&#39;</span><span class="s1">http://43.155.75.36:1069/api.php?do=search&amp;wd={0}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">key</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L110" class="lines-num">
								<span id="L110" data-line-number="110"></span>
							</td>
							<td rel="L110" class="lines-code chroma">
								<code>        <span class="c1"># getHeader()</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L111" class="lines-num">
								<span id="L111" data-line-number="111"></span>
							</td>
							<td rel="L111" class="lines-code chroma">
								<code>        <span class="n">rsp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fetch</span><span class="p">(</span><span class="n">url</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L112" class="lines-num">
								<span id="L112" data-line-number="112"></span>
							</td>
							<td rel="L112" class="lines-code chroma">
								<code>        <span class="n">jo</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">rsp</span><span class="o">.</span><span class="n">text</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L113" class="lines-num">
								<span id="L113" data-line-number="113"></span>
							</td>
							<td rel="L113" class="lines-code chroma">
								<code>        <span class="n">result</span> <span class="o">=</span> <span class="p">{</span><span class="p">}</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L114" class="lines-num">
								<span id="L114" data-line-number="114"></span>
							</td>
							<td rel="L114" class="lines-code chroma">
								<code>        <span class="n">jArray</span> <span class="o">=</span> <span class="p">[</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L115" class="lines-num">
								<span id="L115" data-line-number="115"></span>
							</td>
							<td rel="L115" class="lines-code chroma">
								<code>        <span class="k">if</span> <span class="nb">int</span><span class="p">(</span><span class="n">jo</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">count</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L116" class="lines-num">
								<span id="L116" data-line-number="116"></span>
							</td>
							<td rel="L116" class="lines-code chroma">
								<code>            <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">jo</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">list</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L117" class="lines-num">
								<span id="L117" data-line-number="117"></span>
							</td>
							<td rel="L117" class="lines-code chroma">
								<code>                <span class="n">jArray</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="p">{</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L118" class="lines-num">
								<span id="L118" data-line-number="118"></span>
							</td>
							<td rel="L118" class="lines-code chroma">
								<code>                    <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_id</span><span class="s2">&#34;</span><span class="p">:</span> <span class="n">a</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">id</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L119" class="lines-num">
								<span id="L119" data-line-number="119"></span>
							</td>
							<td rel="L119" class="lines-code chroma">
								<code>                    <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_name</span><span class="s2">&#34;</span><span class="p">:</span> <span class="n">a</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">name</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L120" class="lines-num">
								<span id="L120" data-line-number="120"></span>
							</td>
							<td rel="L120" class="lines-code chroma">
								<code>                    <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_pic</span><span class="s2">&#34;</span><span class="p">:</span> <span class="n">a</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">pic</span><span class="s1">&#39;</span><span class="p">]</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L121" class="lines-num">
								<span id="L121" data-line-number="121"></span>
							</td>
							<td rel="L121" class="lines-code chroma">
								<code>                    <span class="sa"></span><span class="s2">&#34;</span><span class="s2">vod_remarks</span><span class="s2">&#34;</span><span class="p">:</span> <span class="n">a</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">text</span><span class="s1">&#39;</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L122" class="lines-num">
								<span id="L122" data-line-number="122"></span>
							</td>
							<td rel="L122" class="lines-code chroma">
								<code>                <span class="p">}</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L123" class="lines-num">
								<span id="L123" data-line-number="123"></span>
							</td>
							<td rel="L123" class="lines-code chroma">
								<code>        <span class="n">result</span> <span class="o">=</span> <span class="p">{</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L124" class="lines-num">
								<span id="L124" data-line-number="124"></span>
							</td>
							<td rel="L124" class="lines-code chroma">
								<code>            <span class="sa"></span><span class="s1">&#39;</span><span class="s1">list</span><span class="s1">&#39;</span><span class="p">:</span><span class="n">jArray</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L125" class="lines-num">
								<span id="L125" data-line-number="125"></span>
							</td>
							<td rel="L125" class="lines-code chroma">
								<code>        <span class="p">}</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L126" class="lines-num">
								<span id="L126" data-line-number="126"></span>
							</td>
							<td rel="L126" class="lines-code chroma">
								<code>        <span class="k">return</span> <span class="n">result</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L127" class="lines-num">
								<span id="L127" data-line-number="127"></span>
							</td>
							<td rel="L127" class="lines-code chroma">
								<code>    <span class="n">cookie</span> <span class="o">=</span> <span class="p">{</span><span class="p">}</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L128" class="lines-num">
								<span id="L128" data-line-number="128"></span>
							</td>
							<td rel="L128" class="lines-code chroma">
								<code>    <span class="n">config</span> <span class="o">=</span> <span class="p">{</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L129" class="lines-num">
								<span id="L129" data-line-number="129"></span>
							</td>
							<td rel="L129" class="lines-code chroma">
								<code>        <span class="sa"></span><span class="s2">&#34;</span><span class="s2">filter</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">电视剧</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">class</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">剧情</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">剧情</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">剧情</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">古装</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">古装</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">武侠</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">武侠</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">奇幻</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">奇幻</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">科幻</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">科幻</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">动作</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">动作</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">喜剧</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">喜剧</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">爱情</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">爱情</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">励志</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">励志</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">冒险</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">冒险</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">歌舞</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">歌舞</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">音乐</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">音乐</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">恐怖</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">恐怖</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">惊悚</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">惊悚</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">丧尸</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">丧尸</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">战争</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">战争</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">传记</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">传记</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">纪录</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">纪录</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">犯罪</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">犯罪</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">悬疑</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">悬疑</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">西部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">西部</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">灾难</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">灾难</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">家庭</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">家庭</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">短片</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">短片</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">校园</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">校园</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">文艺</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">文艺</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">运动</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">运动</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">青春</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">青春</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">同性</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">同性</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">人性</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">人性</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">美食</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">美食</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">女性</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">女性</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">治愈</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">治愈</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">历史</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">历史</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">area</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">地区</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">大陆</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">大陆</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">香港</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">香港</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">台湾</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">台湾</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">欧美</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">欧美</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">韩国</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">韩国</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">日本</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">日本</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">泰国</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">泰国</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">印度</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">印度</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">俄罗斯</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">俄罗斯</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">其他</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">其他</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">year</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">年份</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2022</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2022</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2021</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2021</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2020</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2020</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2019</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2019</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2018</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2018</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2017</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2017</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2016</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2016</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2015</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2015</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2014</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2014</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2013</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2013</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2012</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2012</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2011</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2011</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2010</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2010</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2009</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2009</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2008</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2008</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2007</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2007</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2006</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2006</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2005</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2005</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2004</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2004</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2003</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2003</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2002</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2002</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2001</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2001</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2000</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2000</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">lang</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">语言</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">英语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">英语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">韩语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">韩语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">日语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">日语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">法语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">法语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">泰语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">泰语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">德语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">德语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">印度语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">印度语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">国语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">国语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">粤 语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">粤语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">俄语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">俄语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">西班牙语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">西班牙语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">意大利语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">意大利语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">其它</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">其它</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">by</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">排序</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">最新</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">time</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">最热</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">hits</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">评分</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">score</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">]</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">电影</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">class</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">剧情</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">剧情</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">剧情</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">古装</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">古装</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">武侠</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">武侠</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">奇幻</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">奇幻</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">科幻</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">科幻</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">动作</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">动作</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">喜剧</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">喜剧</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">爱情</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">爱情</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">励志</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">励志</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">冒险</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">冒险</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">歌舞</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">歌舞</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">音乐</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">音乐</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">恐怖</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">恐怖</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">惊悚</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">惊悚</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">丧尸</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">丧尸</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">战争</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">战争</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">传记</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">传记</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">纪录</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">纪录</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">犯罪</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">犯罪</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">悬疑</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">悬疑</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">西部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">西部</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">灾难</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">灾难</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">家庭</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">家庭</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">短片</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">短片</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">校园</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">校园</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">文艺</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">文艺</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">运动</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">运动</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">青春</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">青春</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">同性</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">同性</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">人性</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">人性</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">美食</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">美食</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">女性</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">女性</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">治愈</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">治愈</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">历史</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">历史</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">year</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">年份</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2022</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2022</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2021</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2021</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2020</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2020</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2019</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2019</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2018</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2018</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2017</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2017</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2016</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2016</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2015</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2015</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2014</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2014</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2013</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2013</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2012</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2012</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2011</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2011</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2010</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2010</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2009</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2009</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2008</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2008</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2006</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2006</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2005</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2005</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2004</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2004</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">lang</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">语言</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">英语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">英语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">法语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">法语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">by</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">排序</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">最新</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">time</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">最热</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">hits</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">评分</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">score</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">]</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">动漫</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">class</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">剧情</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">冒险</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">冒险</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">玄幻</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">玄幻</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">魔幻</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">魔幻</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">武侠</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">武侠</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">恋爱</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">恋爱</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">推理</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">推理</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">日常</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">日常</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">校园</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">校园</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">悬疑</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">悬疑</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">剧情</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">剧情</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">萌系</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">萌系</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">科幻</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">科幻</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">日常</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">日常</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">战斗</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">战斗</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">战争</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">战争</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">热血</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">热血</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">机战</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">机战</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">游戏</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">游戏</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">搞笑</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">搞笑</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">恋爱</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">恋爱</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">后宫</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">后宫</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">百合</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">百合</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">基腐</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">基腐</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">冒险</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">冒险</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">儿童</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">儿童</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">歌舞</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">歌舞</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">音乐</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">音乐</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">奇幻</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">奇幻</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">恐怖</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">恐怖</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">惊悚</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">惊悚</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">犯罪</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">犯罪</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">西部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">西部</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">灾难</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">灾难</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">古装</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">古装</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">泡面</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">泡面</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">运动</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">运动</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">体育</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">体育</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">青春</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">青春</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">美食</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">美食</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">治愈</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">治愈</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">致郁</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">致郁</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">励志</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">励志</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">历史</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">历史</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">真人</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">真人</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">竞技</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">竞技</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">其他</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">其他</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">year</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">年份</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2022</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2022</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2021</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2021</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2020</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2020</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2019</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2019</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2018</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2018</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2017</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2017</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2016</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2016</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2015</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2015</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2014</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2014</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2013</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2013</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2012</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2012</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2011</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2011</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2010</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2010</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2009</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2009</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2008</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2008</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2007</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2007</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2006</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2006</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2005</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2005</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2004</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2004</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2003</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2003</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2002</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2002</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2001</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2001</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2000</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2000</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">by</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">排序</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">最新</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">time</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">最热</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">hits</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">评分</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">score</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">]</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">综艺</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">class</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">剧情</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">游戏</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">游戏</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">音乐</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">音乐</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">养成</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">养成</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">情感</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">情感</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">喜剧</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">喜剧</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">搞笑</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">搞笑</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">脱口秀</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">脱口秀</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">表演</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">表演</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">体验</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">体验</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">亲子</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">亲子</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">文化</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">文化</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">美食</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">美食</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">职场</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">职场</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">体育</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">体育</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">潮流文化</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">潮流文化</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">访谈</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">访谈</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">生活服务</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">生活服务</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">萌宠</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">萌宠</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">资讯</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">资讯</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">曲艺</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">曲艺</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">职场</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">职场</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">晚会</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">晚会</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">year</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">年份</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2022</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2022</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2021</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2021</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2020</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2020</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2019</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2019</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2018</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2018</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2017</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2017</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2016</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2016</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2015</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2015</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2014</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2014</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2013</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2013</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2012</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2012</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2011</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2011</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2010</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2010</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2009</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2009</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2008</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2008</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2007</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2007</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2006</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2006</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2005</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2005</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2004</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2004</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2003</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2003</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2002</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2002</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2001</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2001</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2000</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2000</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">by</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">排序</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">最新</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">time</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">最热</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">hits</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">评分</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">score</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">]</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">记录片</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">class</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">剧情</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">纪录</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">纪录</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">真人秀</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">真人秀</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">自然</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">自然</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">传记</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">传记</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">文化</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">文化</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">情</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">情</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">运动</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">运动</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">area</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">地区</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">国产</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">国产</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">日本</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">日本</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">欧美</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">欧美</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">其他</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">其他</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">lang</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">语言</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">国语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">国语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">日语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">日语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">英语</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">英语</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">其他</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">其他</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">year</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">年份</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">全部</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2022</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2022</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2021</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2021</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2020</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2020</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2019</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2019</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2018</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2018</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2017</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2017</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2016</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2016</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2015</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2015</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2014</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2014</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2013</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2013</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2012</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2012</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2011</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2011</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2010</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2010</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2009</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2009</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2008</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2008</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2007</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2007</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2006</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2006</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2005</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2005</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2004</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2004</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2003</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2003</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2002</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2002</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2001</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2001</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2000</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">2000</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">key</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">by</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">name</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">排序</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">value</span><span class="s2">&#34;</span><span class="p">:</span><span class="p">[</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">最新</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">time</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">最热</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">hits</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">,</span><span class="p">{</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">n</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">评分</span><span class="s2">&#34;</span><span class="p">,</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">v</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">score</span><span class="s2">&#34;</span><span class="p">}</span><span class="p">]</span><span class="p">}</span><span class="p">]</span><span class="p">}</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L130" class="lines-num">
								<span id="L130" data-line-number="130"></span>
							</td>
							<td rel="L130" class="lines-code chroma">
								<code>    <span class="p">}</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L131" class="lines-num">
								<span id="L131" data-line-number="131"></span>
							</td>
							<td rel="L131" class="lines-code chroma">
								<code>    <span class="k">def</span> <span class="nf">playerContent</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">flag</span><span class="p">,</span><span class="nb">id</span><span class="p">,</span><span class="n">vipFlags</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L132" class="lines-num">
								<span id="L132" data-line-number="132"></span>
							</td>
							<td rel="L132" class="lines-code chroma">
								<code>        <span class="k">if</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">STAR@</span><span class="s2">&#34;</span> <span class="ow">in</span> <span class="nb">id</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L133" class="lines-num">
								<span id="L133" data-line-number="133"></span>
							</td>
							<td rel="L133" class="lines-code chroma">
								<code>            <span class="nb">id</span> <span class="o">=</span> <span class="nb">id</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">@</span><span class="s1">&#39;</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L134" class="lines-num">
								<span id="L134" data-line-number="134"></span>
							</td>
							<td rel="L134" class="lines-code chroma">
								<code>            <span class="n">url</span> <span class="o">=</span> <span class="sa"></span><span class="s1">&#39;</span><span class="s1">http://43.155.75.36:1069/api.php?do=Ooo0oo0O0oOo&amp;url={0}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">id</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L135" class="lines-num">
								<span id="L135" data-line-number="135"></span>
							</td>
							<td rel="L135" class="lines-code chroma">
								<code>            <span class="n">rsp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fetch</span><span class="p">(</span><span class="n">url</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L136" class="lines-num">
								<span id="L136" data-line-number="136"></span>
							</td>
							<td rel="L136" class="lines-code chroma">
								<code>            <span class="n">jo</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">rsp</span><span class="o">.</span><span class="n">text</span><span class="p">)</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L137" class="lines-num">
								<span id="L137" data-line-number="137"></span>
							</td>
							<td rel="L137" class="lines-code chroma">
								<code>            <span class="nb">id</span> <span class="o">=</span> <span class="n">jo</span><span class="p">[</span><span class="sa"></span><span class="s1">&#39;</span><span class="s1">url</span><span class="s1">&#39;</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L138" class="lines-num">
								<span id="L138" data-line-number="138"></span>
							</td>
							<td rel="L138" class="lines-code chroma">
								<code>        <span class="n">result</span> <span class="o">=</span> <span class="p">{</span><span class="p">}</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L139" class="lines-num">
								<span id="L139" data-line-number="139"></span>
							</td>
							<td rel="L139" class="lines-code chroma">
								<code>        <span class="n">result</span><span class="p">[</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">parse</span><span class="s2">&#34;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L140" class="lines-num">
								<span id="L140" data-line-number="140"></span>
							</td>
							<td rel="L140" class="lines-code chroma">
								<code>        <span class="n">result</span><span class="p">[</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">playUrl</span><span class="s2">&#34;</span><span class="p">]</span> <span class="o">=</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L141" class="lines-num">
								<span id="L141" data-line-number="141"></span>
							</td>
							<td rel="L141" class="lines-code chroma">
								<code>        <span class="n">result</span><span class="p">[</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">url</span><span class="s2">&#34;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">id</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L142" class="lines-num">
								<span id="L142" data-line-number="142"></span>
							</td>
							<td rel="L142" class="lines-code chroma">
								<code>        <span class="n">result</span><span class="p">[</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">header</span><span class="s2">&#34;</span><span class="p">]</span> <span class="o">=</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L143" class="lines-num">
								<span id="L143" data-line-number="143"></span>
							</td>
							<td rel="L143" class="lines-code chroma">
								<code>        <span class="k">return</span> <span class="n">result</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L144" class="lines-num">
								<span id="L144" data-line-number="144"></span>
							</td>
							<td rel="L144" class="lines-code chroma">
								<code>    <span class="k">def</span> <span class="nf">isVideoFormat</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">url</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L145" class="lines-num">
								<span id="L145" data-line-number="145"></span>
							</td>
							<td rel="L145" class="lines-code chroma">
								<code>        <span class="k">pass</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L146" class="lines-num">
								<span id="L146" data-line-number="146"></span>
							</td>
							<td rel="L146" class="lines-code chroma">
								<code>    <span class="k">def</span> <span class="nf">manualVideoCheck</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L147" class="lines-num">
								<span id="L147" data-line-number="147"></span>
							</td>
							<td rel="L147" class="lines-code chroma">
								<code>        <span class="k">pass</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L148" class="lines-num">
								<span id="L148" data-line-number="148"></span>
							</td>
							<td rel="L148" class="lines-code chroma">
								<code>    <span class="k">def</span> <span class="nf">localProxy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">param</span><span class="p">)</span><span class="p">:</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L149" class="lines-num">
								<span id="L149" data-line-number="149"></span>
							</td>
							<td rel="L149" class="lines-code chroma">
								<code>        <span class="k">return</span> <span class="p">[</span><span class="mi">200</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">video/MP2T</span><span class="s2">&#34;</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">]</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L150" class="lines-num">
								<span id="L150" data-line-number="150"></span>
							</td>
							<td rel="L150" class="lines-code chroma">
								<code>    <span class="n">header</span> <span class="o">=</span> <span class="p">{</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L151" class="lines-num">
								<span id="L151" data-line-number="151"></span>
							</td>
							<td rel="L151" class="lines-code chroma">
								<code>		<span class="sa"></span><span class="s2">&#34;</span><span class="s2">origin</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">https://www.5dy6.vip</span><span class="s2">&#34;</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L152" class="lines-num">
								<span id="L152" data-line-number="152"></span>
							</td>
							<td rel="L152" class="lines-code chroma">
								<code>		<span class="sa"></span><span class="s2">&#34;</span><span class="s2">User-Agent</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36</span><span class="s2">&#34;</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L153" class="lines-num">
								<span id="L153" data-line-number="153"></span>
							</td>
							<td rel="L153" class="lines-code chroma">
								<code>		<span class="sa"></span><span class="s2">&#34;</span><span class="s2">Accept</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2"> */*</span><span class="s2">&#34;</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L154" class="lines-num">
								<span id="L154" data-line-number="154"></span>
							</td>
							<td rel="L154" class="lines-code chroma">
								<code>		<span class="sa"></span><span class="s2">&#34;</span><span class="s2">Accept-Language</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">zh-CN,zh;q=0.9,en-US;q=0.3,en;q=0.7</span><span class="s2">&#34;</span><span class="p">,</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L155" class="lines-num">
								<span id="L155" data-line-number="155"></span>
							</td>
							<td rel="L155" class="lines-code chroma">
								<code>		<span class="sa"></span><span class="s2">&#34;</span><span class="s2">Accept-Encoding</span><span class="s2">&#34;</span><span class="p">:</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">gzip, deflate</span><span class="s2">&#34;</span></code>
							</td>
						</tr>
						
						<tr>
							<td id="L156" class="lines-num">
								<span id="L156" data-line-number="156"></span>
							</td>
							<td rel="L156" class="lines-code chroma">
								<code>	<span class="p">}</span></code>
							</td>
						</tr>
						
					</tbody>
				</table>
				
			
		</div>
	</div>
</div>


	<div class="i-text-center">
		
				
		
	</div>


<script>
function submitDeleteForm() {
    var message = prompt("delete_confirm_message\n\ndelete_commit_summary", "Delete ''");
    if (message != null) {
        $("#delete-message").val(message);
        $("#delete-file-form").submit()
    }
}
</script>

		
	</div>
	<div id="toListModel">
		<div class="ui modal" id="toShare">
			<i class="close icon black"></i>
			<div class="header">Share Source</div>
			<div class="content">
				<form autocomplete="off" class="ui form training ignore-dirty">
					
					<div class="fields">
						<p class="px-sm py-none mb-sm">Sharing will generate an anonymous link to present the selected codes and training results, which will not reveal the original repository address. However, Agit cannot process the codes or the training results. For double-blind peer review or similar usages, please ensure the contents have been fully anonymized.</p>
					</div>

					<div class="fields">
						<div class="two wide field required">
							<label>Branch</label>
						</div>
						<div id="branchField" class="fourteen wide field">

							<div class="fitted item choose">
								<div class="ui floating filter dropdown custom">

									<div class="ui basic small compact button" style="min-width: 200px;" @click="menuVisible = !menuVisible">
										<span class="text">
											<i class="iconfont icon-branch-down"></i>
											<span v-text='isViewBranch?"Branch":"Tree"'></span>:
                      <strong v-text='isViewBranch?(selectedBranch?selectedBranch:"Please select"):(selectedTag?selectedTag:"Please select")'></strong>
										</span>
										<i class="dropdown icon" tabIndex="-1"></i>
									</div>

									<div tabindex="-1"  id="scrolling" class="menu transition menu-share" :class="{visible: menuVisible}" v-show="menuVisible" @blur="menuVisible = false">

										<div class="ui icon search input" style="width: 200px;">
											<i class="filter icon"></i>
											<input name="search" v-model="searchTerm" @keydown="keydown($event)" placeholder="Filter branch or tag...">
										</div>

										<div class="header branch-tag-choice">
											<div class="ui grid">
												<div class="two column row">
													<a class="reference column" href="javascript:;" @click="handleBranchTab(true)">
														<span class="text" :class="{black: !isViewBranch}">
															<i class="iconfont icon-branch-down"></i>
															Branches
														</span>
													</a>
													<a class="reference column" href="javascript:;" @click="handleBranchTab(false)">
														<span class="text" :class="{black: isViewBranch}">
															<i class="reference tags icon"></i>
															Tags
														</span>
													</a>
												</div>
											</div>
										</div>

										<div v-show="isViewBranch" class="scrolling menu" ref="scrollContainer">
											<div v-for="(item, index) in branches" v-show="item.name.includes(searchTerm)" :key="item.name" class="item" @click="handleBranchOrTag(item)">
												<span v-text="item.name"></span>
											</div>
										</div>
										<div v-show="!isViewBranch" class="scrolling menu" ref="scrollContainer">
											<div v-for="(item, index) in tags" v-show="item.name.includes(searchTerm)" :key="item.name" class="item" @click="handleBranchOrTag(item)">
												<span v-text="item.name"></span>
											</div>
										</div>

										<div class="message" v-if="(isViewBranch && branches.length==0) || (!isViewBranch && tags.length==0)">No results found.</div>
									</div>

									<div class="ui pointing red basic label" style="display:none;">
										Please select a branch or tag
									</div>

								</div>
							</div>
						</div>
					</div>

					<div class="fields" v-show="selectedBranch">
						<div class="two wide field">
							<label>Commit</label>
						</div>
						<div id="commitWrap" class="fourteen wide field">
							<select class="ui search selection dropdown commit-wrap" name="commit">
								<option value=""></option>
							</select>
						</div>
					</div>
					<div class="fields">
						<label class="two wide field  required">Share Title</label>
						<div class="fourteen wide field trainName-filed">
							<input v-model="shareName" type="text" name="shareName"  class="form-trainName" :maxlength="16"  placeholder="Please enter the title content, limited to 16 bits">
						</div>
					</div>
					<div class="ui grid uioption">
						<label class="required">Link Validity</label>
					</div>
					<div class="ui grid fields">
						<div class="thirteen wide column">
							<div class="ui four item stackable tabs menu ui-link-bg">
								<a v-for="(item, index) in shareTimeList" :key="index" :class="['item', activeIdx === item.shareTimeId ? 'active' : '']" data-tab="oneday" @click="handleMenuChange(item)">
									<span v-text="formatLinkTime(item.shareTimeName)"></span></a>
							</div>
						</div>
						<div class="right aligned three wide column action mt-3xs">
							<button class="ui primary button" @click="handleLink">
								Generate Link</button>
						</div>
					</div>
				</form>
			</div>
		</div>
		<div class="ui modal" id="toCopyShareLink">
			<i class="close icon black"></i>
			<div class="header">Share link has been generated</div>
			<div class="content ui form">
				<div class="fields">
					<div class="two wide field">
						<label>Link Address:</label>
					</div>
					<div  class="fourteen wide field">
						<p v-text="linkAddress" id="share_url"></p>
					</div>
				</div>
				<div class="fields uioption">
					<div class="two wide field">
					<label>Link Validity:</label>
					</div>
					<div class="fourteen wide field">
						<p v-text="linkExDate"></p>
					</div>
				</div>
				<div class="fields uioption">
							<div class="sixteen wide field" style="text-align: right">
								<button class="ui basic icon button poping primary up clipboard share-button" id="share-button" data-original="Copy" data-success="Link has been copied" data-error="Use ⌘C or Ctrl-C to copy" data-content="Copy" data-variation="inverted tiny"  data-clipboard-target="#share_url">
									Copy Share
								</button>
							</div>
				</div>

			</div>
		</div>
	</div>

</div>
<div class="content">
	<p></p>
</div>
</div>
</div>




		

		</div>

		

		<footer>
	<div class="base-footer-content i-footer mx-auto">
		<div class="ui left">
			<div class="p-logo i-flex i-align-center">
				<img class="logo-icon" src="/img/logo/logo.svg">
				<i class="logo-text">&copy; 2023 Agit Cloud Computing, Ltd.</i>
				<a  id="version-a" style="margin-right: 16px; text-decoration: underline; font-size: 12px;" target="_blank" href="https://agit.ai/AgitDeveloper/AgitPythonExamples/wiki"></a>
			</div>
		</div>
		<div class="ui right links p-logo">
			<a style="margin-right: 16px; text-decoration: underline; font-size: 12px;" target="_blank" href="/agreement/terms">Terms of Service</a>
<a style="margin-right: 16px; text-decoration: underline; font-size: 12px;" target="_blank" href="/agreement/privacy">Privacy Statement</a>
<a style="text-decoration: underline; font-size: 12px; margin-right: 16px;" target="_blank" href="/opensource">Open Source</a>
<a style="text-decoration: underline; font-size: 12px;" target="_blank" id="help-a" target="_blank" href="http://help.agit.ai/">Help</a>

		</div>
	</div>
</footer>



		

		
		
		
		<script src="/js/index.js?v=220846678a86246c9d7e7c46c21f20c2"></script>

		<script src="/vendor/plugins/vue/vue.min.js"></script>
<script src="/minifyjs/head_navbar.base.js?v=220846678a86246c9d7e7c46c21f20c2"></script>
<script src="/minifyjs/footer_content.base.js?v=220846678a86246c9d7e7c46c21f20c2"></script>


<script src="/vendor/plugins/promise-polyfill/polyfill.min.js"></script>
<script src="/vendor/plugins/cssrelpreload/loadCSS.min.js"></script>
<script src="/vendor/plugins/cssrelpreload/cssrelpreload.min.js"></script>
<script src="/vendor/plugins/vue-infinite-loading/vue-infinite-loading.js?v=220846678a86246c9d7e7c46c21f20c2"></script>
<script src="/vendor/plugins/Qrcode/qrcode.min.js?v=220846678a86246c9d7e7c46c21f20c2"></script>
<script src="/vendor/plugins/i-components/i.components.min.js?v=220846678a86246c9d7e7c46c21f20c2"></script>

<script src="/vendor/plugins/vue-node-spec/node-spec.min.js?v=220846678a86246c9d7e7c46c21f20c2"></script>
<script src="/vendor/plugins/jquery-migrate/jquery-migrate.min.js?v=3.0.1"></script>
<script src="/vendor/plugins/jquery.areyousure/jquery.are-you-sure.js"></script>
<script src="/vendor/plugins/emojify/emojify.custom.js"></script>
<script src="/vendor/plugins/xterm/xterm.js"></script>









	</body>
	</html>

<script>
$("#createTraining").click(function(){

	$api.trainReachUpperLimit({repoId:Number($('.repo-id').text())}).then(data => {
        if (!data) return;
		if(data.isUpperLimit){
			$ITools.handleToast('error', $i18n.tr('code', 'trainCountLimit'))
			return
		}

		const mode = $("#branchSelect").attr("data-mode"),
	      	branch = $("#branchSelect").find("strong").text();
		let path = ""
		$(".repo-path a").each(function(index,item){
			if(index === 0){
				return
			}
			path += path === ""?$(this).attr("title"):("/"+$(this).attr("title"))
		})
		const params={
			scriptPath: $(".repo-path").find(".active.section").attr("title"),
			workSpace: path,
			branchName: mode === "branches" ? branch : "",
			tagName: mode === "branches" ? "" : branch
		}
		window.location.href = window.location.origin + $('.repo-url').text() + '/training/create?scriptFile=' + escapePound(JSON.stringify(params))
      })


})
function toUpload(el) {

const tempSplit = $("#RepoSize").text().split("GB")


if (tempSplit.length === 2 && tempSplit[0] >= 1) {
	$ITools.handleToast('error', $i18n.tr('valid', 'fileSizeLimit'))
	return
}
window.location.href = $(el).attr("data-href")
}
function handleShare() {
$('#toShare').modal('show')
}
function shareLink() {
$('#toCopyShareLink').modal('show')
}
function escapePound(str){
	let res=""
	res=str.replaceAll("%","%25")
	res=res.replaceAll("#","%23")
	res=res.replaceAll(" ","%20")
	res=res.replaceAll("?","%3F")
	return res
}
</script>

<script src="/minifyjs/auth.js?v=220846678a86246c9d7e7c46c21f20c2"></script>
<script src="/minifyjs/repo_home.js?v=220846678a86246c9d7e7c46c21f20c2"></script>

